""" This script fetches data from both MariaDB and InfluxDB. """

from src.data_extraction import fetch_mariadb_data, fetch_influxdb_data


def main():
    """
    Executes the main function which fetches data from both MariaDB and InfluxDB.

    This function does not take any parameters.

    This function does not return any value.

    This function calls the `fetch_mariadb_data()` function to fetch data from MariaDB and the `fetch_influxdb_data()` function to fetch data from InfluxDB.

    Note: This function assumes that the necessary functions `fetch_mariadb_data()` and `fetch_influxdb_data()` are defined elsewhere in the codebase.

    """
    fetch_mariadb_data()
    fetch_influxdb_data()


if __name__ == "__main__":
    main()
