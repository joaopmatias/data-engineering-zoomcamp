
import os
import sys
import argparse

from pathlib import Path
from collections import defaultdict

import pandas as pd
import numpy as np

from sqlalchemy import create_engine


def main(params):
    file_name = params.file_name
    table_name = params.table_name
    if_exists = params.if_exists


    engine = create_engine(
        f"""postgresql://{os.getenv("POSTGRES_USER")}"""
        f""":{os.getenv("POSTGRES_PASSWORD")}"""
        f"""@{os.getenv("POSTGRES_HOST")}"""
        f""":{os.getenv("POSTGRES_PORT")}"""
        f"""/{os.getenv("POSTGRES_DB")}""")
    
    functions = defaultdict(
        lambda: (lambda x: x),
        tpep_pickup_datetime=lambda s: pd.to_datetime(s),
        tpep_dropoff_datetime=lambda s: pd.to_datetime(s),
        lpep_pickup_datetime=lambda s: pd.to_datetime(s),
        lpep_dropoff_datetime=lambda s: pd.to_datetime(s),
        VendorID=lambda s: s.astype(np.int32),
        RatecodeID=lambda s: s.astype(np.int32),
        passenger_count=lambda s: s.astype(np.int32),
        PULocationID=lambda s: s.astype(np.int32),
        DOLocationID=lambda s: s.astype(np.int32),
        payment_type=lambda s: s.astype(np.int32),
        LocationID=lambda s: s.astype(np.int32),
        trip_type=lambda s: s.astype(np.int32),
    )

    file = Path("/home/datasets") / file_name
    (
        pd.read_csv(file, nrows=100)
        .pipe(
            lambda ddf:
            ddf.assign(**{k: functions[k](ddf[k]) for k in ddf.columns}))
        .loc[[]]
        .to_sql(name=table_name, con=engine, if_exists=if_exists, index=False)
    )

    for df in pd.read_csv(file, iterator=True, chunksize=100_000):
        print(df.head(1))
        (
            df
            .pipe(
                lambda ddf:
                ddf.assign(**{k: functions[k](ddf[k]) for k in ddf.columns}))
            .to_sql(name=table_name, con=engine, if_exists="append", index=False)
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest CSV data to Postgres")
    parser.add_argument("--file_name", help="Name of the CSV file.", required=True)
    parser.add_argument("--table_name", help="Name of the destination table.", default="yellow_taxi_data")
    parser.add_argument("--if_exists", help="Behavior when the table already exists in the database.", default="append")

    args = parser.parse_args()

    main(args)
