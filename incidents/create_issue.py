"""Create_issue takes the sections from the config file, along with the options passed from parse_config. Based on what section is passed, the program should create a ticket specifically for that section (issue tracking platform)."""

import os
from jira import JIRA
import sys
import logging

logging.basicConfig(level=logging.DEBUG)

class Ticket(object):
    """Class responisble for creating ticket/issue on specified platform."""
    def __init__(self, **kwargs):
        #Initialize the allowed_keys as False.
        #Update the allowed_keys with the values passed from __main__.py.
        allowed_keys = {'config_info', 'group_name', 'description', 'summary', 'upload', 'user'}
        self.__dict__.update((key, False) for key in allowed_keys)
        self.__dict__.update((key, value) for key, value in kwargs.items() if key in allowed_keys)
        self.priority = 'Top'
        self.real_groups = ('project_1-jira', 'project_2-jira', 'project_3-jira', 'mnt-issue_log')
        #Connecting to jira api using JIRA-python package.
        try:
            self.jira = JIRA(self.config_info[self.group_name]['host'], auth=(self.config_info[self.group_name]['user'],self.config_info[self.group_name]['passwd']))
        except Exception as e:
            print(e)

    def create_jira_Ticket(self):
        """Creating jira ticket."""
        print('Creating Ticket')
        #Information from both config and user input for creating ticket in Jira.
        issue_fields = {
                'project': {'key' : self.config_info[self.group_name]['project']},
                'summary': self.config_info[self.group_name]['component'] + ' - ' + self.summary ,
                'description': self.description,
                'issuetype': {'name': self.config_info[self.group_name]['issue_level']},
                'priority': {'name': 'Top'},
                'components': [{'name': self.config_info[self.group_name]['component']}],
                    }

        #Creating the actual ticket.
        try:
            jira_issue = self.jira.create_issue(fields=issue_fields)
            asigned_to = self.jira.assign_issue(jira_issue, self.config_info[self.group_name]['user'])
            print("Jirra issue: {}".format(jira_issue))
        except Exception as e:
            print(e)

        #Check self.upload for file to upload.
        if not self.upload:
            pass
        else:
            self.upload_attachment(jira_issue)

    def upload_attachment(self, jira_issue):
        #If specified, file upload to jira ticket just created.
        try:
            self.jira.add_attachment(issue=jira_issue, attachment=self.upload)
        except Exception as e:
            print(e)
