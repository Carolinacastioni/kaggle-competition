import pandas as pd


def open_file(file):
    df = pd.read_csv(file, error_bad_lines=False)
    return df

