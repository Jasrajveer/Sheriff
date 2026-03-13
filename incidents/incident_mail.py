import subprocess
import requests

class IncidentMailError(Exception):
    """Raised when email recipient lookup or send operation fails."""


#Default list for emails from Config file, as well as specifying the database_email edpoint which returns email list from database.
class Incident_mail():
    def __init__(self, summary, description, database_email_group, default_email_group):
        self.summary = str(summary)
        self.description = description or ""

        if not database_email_group:
            self.email_group = default_email_group
            return


        try:
            response = requests.get('some web address here' + database_email_group, timeout=10)
            response.raise_for_status()

            if response.text != 'Error: list name not selected':
                self.email_group = response.text.strip()
            else:
                self.email_group = default_email_group

        except requests.RequestException:
            self.email_group = default_email_group

    def send_mail(self):
        if self.email_group == "":
            print("No email specified or pulled.")
        else:
            try:
                subprocess.run(
                        ['mail', '-s', self.summary, self.email_group],
                        input=self.description,
                        text=True,
                        check=True
                )

            except subprocess.SubprocessError as e:
                raise IncidentMailError(f'Failed to send email notification: {e}') from e


