""" Data processing utilities. """

import pandas as pd
from sklearn.preprocessing import MinMaxScaler


def preprocess_data():
    """
    Preprocesses the data by reading the raw data from both MariaDB and InfluxDB,
    concatenating the dataframes, dropping any rows with missing values, scaling the
    features using MinMaxScaler, and creating a dummy example for presence.
    Finally, the preprocessed data is saved to a CSV file.

    Parameters:
    None

    Returns:
    None
    """
    df_mariadb = pd.read_csv("data/raw/mariadb_data.csv")
    df_influxdb = pd.read_csv("data/raw/influxdb_data.csv")
    df_combined = pd.concat([df_mariadb, df_influxdb], ignore_index=True).dropna()

    scaler = MinMaxScaler()
    features = ["motion", "temperature", "humidity", "luminance"]
    df_combined[features] = scaler.fit_transform(df_combined[features])

    # Dummy example for presence
    df_combined["presence"] = df_combined["motion"]
    df_combined.to_csv("data/processed/combined_data.csv", index=False)
