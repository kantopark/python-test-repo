import pandas as pd


def transform():
    cars = pd.read_csv("/output/cars.csv")
    cars *= 2

    cars.to_csv("/output/transformed_cars.csv")

    print("transform ran successfully")


if __name__ == '__main__':
    transform()
