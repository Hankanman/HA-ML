""" Data extraction utilities. """

import pymysql as sql
import pandas as pd
from influxdb_client import InfluxDBClient
from config import load_config


def fetch_mariadb_data():
    config = load_config()
    mariadb_config = config["mariadb"]
    sensors = config["sensors"]["mariadb"]
    date_range = config["date_range"]

    connection = sql.connect(
        host=mariadb_config["host"],
        user=mariadb_config["user"],
        password=mariadb_config["password"],
        database=mariadb_config["database"],
    )

    query = f"""
    SELECT timestamp, {', '.join(sensors)}
    FROM your_table
    WHERE timestamp BETWEEN '{date_range['start']}' AND '{date_range['end']}'
    """
    df = pd.read_sql(query, connection)
    connection.close()
    df.to_csv("data/raw/mariadb_data.csv", index=False)


def fetch_influxdb_data():
    config = load_config()
    influxdb_config = config["influxdb"]
    sensors = config["sensors"]["influxdb"]

    client = InfluxDBClient(
        url=influxdb_config["url"],
        token=influxdb_config["token"],
        org=influxdb_config["org"],
    )

    query = f"""
    from(bucket: "{influxdb_config['bucket']}")
    |> range(start: {date_range['start']}, stop: {date_range['end']})
    |> filter(fn: (r) => r._measurement == "your_measurement")
    |> filter(fn: (r) => contains(value: r._field, set: {sensors}))
    |> pivot(rowKey:["_time"], columnKey: ["_field"], valueColumn: "_value")
    """
    result = client.query_api().query_data_frame(query)
    df = result[sensors]
    df.to_csv("data/raw/influxdb_data.csv", index=False)
