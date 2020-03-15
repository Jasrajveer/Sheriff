import os
import datetime
import json

class Statistics(object):
    def __init__(self, stat_file_path, summary):
        self.path = os.path.join(stat_file_path + 'stat_file.txt')
        self.summary = summary
        self.time = str(datetime.datetime.utcnow())

    def write_file(self):
        if os.path.exists(self.path) == True:
            with open(self.path, 'r') as stat_file:
                failure_info = json.load(stat_file)
                if self.summary in list(failure_info):
                    failure_info[self.summary]['frequency'] += 1
                else:
                    failure_info[self.summary] = {'frequency': 1, 'date': self.time}
            with open(self.path, 'w') as write_new:
                write_new.write(json.dumps(failure_info, indent=4) + '\n')
        else:
            with open(self.path, 'a+') as new_file:
                failure_dict = {
                self.summary : {'frequency': 1, 'date': str(datetime.datetime.utcnow())}
                }
                new_file.write(json.dumps(failure_dict, indent=4))
