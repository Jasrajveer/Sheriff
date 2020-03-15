"""Reads config file for specified incident tracking platforms(sections), groups them with the
options passed from __main__.py. For each section in the config file, the section and the options
are passed to create_issue.py to create the actual issue. """

import yaml

def parse_yaml(config_path):
    '''Parse the config file passed.'''
    try:
        with open(config_path, 'r') as config_file:
            config_data = yaml.safe_load(config_file)
        return config_data
    except Exception as config_error:
        print(f'Issue loading config file: {config_error}')
