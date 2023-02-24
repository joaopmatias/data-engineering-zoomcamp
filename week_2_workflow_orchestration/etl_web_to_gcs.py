import os
from pathlib import Path
import pandas as pd
from prefect import flow, task
from prefect_gcp.cloud_storage import GcsBucket
from prefect.filesystems import LocalFileSystem
from random import randint


@task(retries=3, log_prints=True)
def fetch(dataset_url: str) -> pd.DataFrame:
    """Read taxi data from web into pandas DataFrame"""
    # if randint(0, 1) > 0:
    #     raise Exception

    df = pd.read_csv(dataset_url)
    return df


@task(log_prints=True)
def clean(df: pd.DataFrame) -> pd.DataFrame:
    """Fix dtype issues"""
    df = (
        df
        .assign(**{c: pd.to_datetime(df[c]) for c in df.columns if "datetime" in c})
    )
    print(df.head(2))
    print(f"columns: {df.dtypes}")
    print(f"rows: {len(df)}")
    return df


@task(log_prints=True)
def write_local(df: pd.DataFrame, color: str, dataset_file: str) -> Path:
    """Write DataFrame out locally as parquet file"""
    path = Path(f"data/{color}/{dataset_file}.parquet")
    os.makedirs(path.parent, exist_ok=True)
    df.to_parquet(path, compression="gzip")
    LocalFileSystem(basepath=".").get_directory(path.as_posix(), path.as_posix())
    print(path.resolve())
    return path


@task(log_prints=True)
def write_gcs(path: Path) -> None:
    """Upload local parquet file to GCS"""
    gcs_block = GcsBucket.load("zoom-gcs")
    gcs_block.upload_from_path(from_path=path, to_path=path)
    print(path.resolve())
    return


@flow(name="web_to_gcs", log_prints=True)
def etl_web_to_gcs(
    color: str,
    year: int,
    month: int,
) -> None:
    """The main ETL function"""
    dataset_file = f"{color}_tripdata_{year}-{month:02}"
    dataset_url = f"https://github.com/DataTalksClub/nyc-tlc-data/releases/download/{color}/{dataset_file}.csv.gz"

    df = fetch(dataset_url)
    df_clean = clean(df)
    path = write_local(df_clean, color, dataset_file)
    write_gcs(path)

#
#  if __name__ == "__main__":
#      etl_web_to_gcs()
#