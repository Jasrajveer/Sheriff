"""Reads config file for specified incident tracking platforms(sections), groups them with the
options passed from __main__.py. For each section in the config file, the section and the options
are passed to create_issue.py to create the actual issue. """

import os
import yaml


def parse_yaml(config_path):
    '''Parse the config file passed.'''
    if not config_path:
        raise ValueError('Config path is required.')

    if not os.path.exists(config_path):
        raise FileNotFoundError('Config file does not exist: {config_path}')

    try:
        with open(config_path, 'r', encoding='utf-8') as config_file:
            config_data = yaml.safe_load(config_file)
    except yaml.YAMLError as config_error:
            raise ValueError(f'Invalid YAML config file: {config_error}') from config_error

    if not isinstance(config_data, dict):
        raise ValueError(f'Config file must contain a mapping of groups to configuration values.')

    return config_data
