import os

import pandas as pd
from sqlalchemy import create_engine


def get_engine():
    uid = os.getenv("POSTGRES_USER")
    pwd = os.getenv("POSTGRES_PASSWORD")

    host = os.getenv("POSTGRES_HOST")
    port = os.getenv("POSTGRES_PORT")
    db = os.getenv("POSTGRES_DB")

    return create_engine(f"postgres://{uid}:{pwd}@{host}:{port}/{db}")


def save():
    engine = get_engine()
    df = pd.read_csv("/output/transformed_cars.csv")
    df.to_sql("cars", engine)


if __name__ == '__main__':
    save()
