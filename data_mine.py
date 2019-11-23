import pandas as pd

from constants import MovieGross
from utils import get_root_dir

ROOT_DIR = get_root_dir()


class DataOverview:
    def __init__(self):

        self.train_data = MovieGross.TRAIN_DATA
        self.body = pd.DataFrame()

    def load_data(self):

        # load the data onto the body df
        self.body = pd.read_csv("{}/data/{}".format(ROOT_DIR, self.train_data))
        return self.body

    def show_nulls(self):

        null_values = []
        total_records = self.body.shape[0]

        for column in self.body:

            null_counts = self.body[column].isna().sum()
            null_percents = null_counts / total_records
            data_to_append = (column, null_counts, null_percents)
            null_values.append(data_to_append)

        labels = ["header", "counts", "percents"]
        null_df = (
            pd.DataFrame()
            .from_records(null_values, columns=labels)
            .set_index("header")
            .sort_values(by=["counts"], ascending=False)
        )

        return null_df

    def explore_columns(self):


    def handle(self):

        self.load_data()
        a = self.show_nulls()
        print(a)


test = DataOverview()
test.handle()
