import os
import sys
import datetime
import json


def create_log(config_info, group_name, description, summary, user):
    """Creating log issue."""
    #Setting path and file name for log file.
    log_location = config_info[group_name]['path']
    comp_name = config_info[group_name]['component']
    path = os.path.join(log_location, comp_name + '.log')
    

    log_data = {
    'date': str(datetime.datetime.utcnow()),
    'Summary': summary,
    'Description': description,
    }
    #Open and create log file.
    with open(path, 'a+') as log_file:
        log_file.write(json.dumps(log_data) + '\n')
    print('Log file created for failure at: {}'.format(path))
