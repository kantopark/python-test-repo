import pandas as pd
import os


def get_cars_data():
    fn = os.getenv("file_name")
    if fn is None:
        raise ValueError("file_name is not defined")

    df = pd.read_csv(f"https://raw.githubusercontent.com/kantopark/python-test-repo/master/data/{fn}")

    # /output is a mounted volume in the docker container
    df.to_csv("/output/cars.csv")


if __name__ == '__main__':
    get_cars_data()
