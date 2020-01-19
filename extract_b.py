import requests


class DataFetchException(Exception):
    def __init__(self, source: str):
        super().__init__(f"could not fetch data from source '{source}'")


def get_mt_cars_data():
    source = "https://raw.githubusercontent.com/kantopark/python-test-repo/master/data/mtcars.csv"
    resp = requests.get(source)
    if resp.status_code != 200:
        raise DataFetchException(source)

    content = []

    # read csv content
    for i, line in enumerate(resp.text.split("\n")):
        parts = line.strip().split(",")
        if i == 0:
            # first row is header
            content.append(parts)
        else:
            # first column is string, the rest are int
            content.append([j if i == 0 else int(j) for i, j in enumerate(parts)])

    with open("/output/mtcars.csv", "w+") as f:
        f.write("\n".join(content))

    print("get_mt_cars_data ran successfully")


if __name__ == '__main__':
    get_mt_cars_data()
