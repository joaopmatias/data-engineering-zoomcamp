from pathlib import Path
import pandas as pd
from prefect import flow, task
from prefect_gcp.cloud_storage import GcsBucket
from prefect_gcp import GcpCredentials


@task(retries=3)
def extract_from_gcs(color: str, year: int, month: int) -> Path:
    """Download trip data from GCS"""
    gcs_path = f"data/{color}/{color}_tripdata_{year}-{month:02}.parquet"
    gcs_block = GcsBucket.load("zoom-gcs")
    gcs_block.get_directory(from_path=gcs_path, local_path=f".")
    return Path(f"{gcs_path}")


@task()
def transform(path: Path) -> pd.DataFrame:
    """Data cleaning example"""
    df = pd.read_parquet(path)
    if "passenger_count" in df.columns:
        print(f"pre: missing passenger count: {df['passenger_count'].isna().sum()}")
        df["passenger_count"].fillna(0, inplace=True)
        print(f"post: missing passenger count: {df['passenger_count'].isna().sum()}")
    if "PULocationID" in df.columns:
        print(f"pre: missing passenger count: {df['PULocationID'].isna().sum()}")
        df["PULocationID"].fillna(0, inplace=True)
        print(f"post: missing passenger count: {df['PULocationID'].isna().sum()}")
    return df


@task(log_prints=True)
def write_bq(df: pd.DataFrame, table: str) -> None:
    """Write DataFrame to BiqQuery"""

    gcp_credentials_block = GcpCredentials.load("zoom-gcp-creds")

    df.to_gbq(
        destination_table=f"dezoomcamp.{table}",
        project_id="taxi-rides-ny-373121",
        credentials=gcp_credentials_block.get_credentials_from_service_account(),
        chunksize=500_000,
        if_exists="append",
    )


@flow(name="gcs_to_bq", log_prints=True)
def etl_gcs_to_bq(
    color: str,
    year: int,
    month: int,
):
    """Main ETL flow to load data into Big Query"""

    path = extract_from_gcs(color, year, month)
    df = transform(path)
    write_bq(df, color)

#
#  if __name__ == "__main__":
#      etl_gcs_to_bq()
#