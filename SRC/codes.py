import pandas as pd


def open_file(file):
    df = pd.read_csv(file, error_bad_lines=False)
    return df

def get_len(pred):
    return len(pred)

