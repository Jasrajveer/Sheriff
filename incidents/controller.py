"""
Controller is responsible for dictating which specific task to run based on user input. Also allows for
user to import incidents into python scripts.
"""
import sys
import os
import requests
from incidents import parse_config
from incidents.create_issue import Ticket
from incidents.makeLog import create_log
from incidents.stats import Statistics
from incidents.incident_mail import Incident_mail

class Controller(object):
    """Based on user input will create Jira ticket, store in log, or both. The default setting is to always send out an email
    based on which component fails. New supported platforms will be added to type_dispatch."""
    def __init__(self, **kwargs):
        allowed_keys = {'config', 'description', 'summary', 'upload', 'groups', 'path'}
        self.__dict__.update((key, False) for key in allowed_keys)
        self.__dict__.update((key, value) for key, value in kwargs.items() if key in allowed_keys)
        self.config_data = parse_config.parse_yaml(self.config)
        self.user = os.getlogin()
        self.type_dispatch = {
        'jira': self._sendJira,
        'log_file': self._sendLog
        }

    def load_platform(self):
        for group in self.groups:
            try:
                #Group name is passed in by user and all info specified within config will be used to create Ticket/Log.
                self.type_dispatch[self.config_data[group]['type']](specific_group=group)
            except Exception as e:
                print(e)
            try:
                #If databse email list is unavailable it will use default email specified in config.
                self._sendMail(self.config_data[group]['database_email_list'], self.config_data[group]['database_email_list'])
            except Exception as e:
                print(e)
            try:
                #Create stat file, currrently supports frequency of failures based on summary input.
                self._runStat(self.config_data[group]['path'])
            except Exception as e:
                print(e)

    def _sendJira(self, specific_group):
        #Send information to jira module to create ticket.
        Ticket(config_info=self.config_data, group_name=specific_group,
        description=self.description, summary=self.summary,
        user=self.user, upload=self.upload).create_jira_Ticket()


    def _sendLog(self, specific_group):
        #Create log file.
        create_log(config_info=self.config_data, group_name=specific_group,
        description=self.description, summary=self.summary,
        user=self.user)

    def _runStat(self, stat_file_path):
        try:
            Statistics(stat_file_path, self.summary).write_file()
        except Exception as e:
            print(e)

    def _sendMail(self, database_email_group, default_email_group):
        try:
            Incident_mail(self.summary, self.description, database_email_group, default_email_group).send_mail()
        except Exception as e:
            print(e)
