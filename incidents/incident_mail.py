import os
import sys
import requests


#Default list for emails from Config file, as well as specifying the database_email edpoint which returns email list from database.
class Incident_mail():
    def __init__(self, summary, description, database_email_group, default_email_group):
        self.summary = str(summary)
        self.description = description

        response = requests.get('https://random.com/emails/email_list?list_name=' + database_email_group)
        if response.status_code == 200:
            if response.text != 'Error: list name not selected':
                self.email_group = response.text
            else:
                self.email_group = default_email_group
        else:
            self.email_group = default_email_group

    def send_mail(self):
        cmd = "echo " + self.description + " | mail -s " + self.summary  + " " + self.email_group
        #print(self.email_group)
        #print(cmd)
        try:
            os.system(cmd)
        except Exception as e:
            print(e)

