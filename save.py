import os

import pandas as pd
from sqlalchemy import create_engine


def get_engine():
    uid = os.getenv("DB_USERNAME")
    pwd = os.getenv("DB_PASSWORD")

    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")

    return create_engine(f"postgres://{uid}:{pwd}@{host}:{port}/postgres")


def save():
    engine = get_engine()
    df = pd.read_csv("/output/transformed_cars.csv")
    df.to_sql("cars", engine)


if __name__ == '__main__':
    save()
