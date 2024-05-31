""" Configuration utilities. """

import yaml


def load_config(config_path="config/config.yaml"):
    """
    Load a YAML configuration file and return its contents as a dictionary.

    Args:
        config_path (str, optional): The path to the configuration file. Defaults to 'config/config.yaml'.

    Returns:
        dict: The contents of the configuration file as a dictionary.

    Raises:
        FileNotFoundError: If the specified configuration file does not exist.
        yaml.YAMLError: If there is an error parsing the YAML file.

    """
    with open(config_path, "r", encoding="utf-8") as file:
        config = yaml.safe_load(file)
    return config
