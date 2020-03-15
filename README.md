# Introduction
Incidents is a command line tool used for creating issues on multiple incident tracker platforms such as Jira. Create issues/tickets on multiple platforms (currently supports Jira), and storing on a file system. Incidents can be used as either a command line tool or import as python module. The platforms are specified on the `config.yml` file.
There are some bits of the code you would have to change which includes project names that are in Jira, and host url. This will be updated soon so that the only changes that would need to be made are you specifications on the config yaml file. 

## Install
Go into incidents directory and 'run pip install .' .

## Config File (Required)
A template config file is provided with example groups, which contain the type of platform on which you want the ticket to be created as well as the required credentials. The groups that will be executed are set by the -n option.  

## Using as python module
```
from incidents.controller import Controller

#Specify a path to your config file.
path = os.path.join('Example/path/config.yml')
Controller(config=path, description= 'Example as module for python.', summary='Python module test for incidents.', groups = ['mnt-issue_log', 'DSS-jira']).load_platform()

```

## Running in command line
- There are four required options that for creating an issue. Those are summary, description, path to user config file, and project name(s).
2To get started, use the -h option: `incidents -h`.

Output:
```
-h, --help            show this help message and exit
-d DESCRIPTION, --description DESCRIPTION
                      Description of the failure/error.
-s SUMMARY, --summary SUMMARY
                      Summary for the issue/ticket.
-p PATH, --path PATH  Path to config file.
-u UPLOAD_FILE, --upload_file UPLOAD_FILE
                      Path to file for uploading to jira ticket.
-n PROJECT_NAME [PROJECT_NAME ...], --project_name PROJECT_NAME [PROJECT_NAME ...]
                      Project name for preset information in Config.
```

After running the program, you should get the issue id printed on the screen.

## Example Run

```
$ incidents -s "Testing command line tool." -d "This is an example for the readme." -p "Path to config" -n "DSS-jira"
Expected Output:
DSS-{Issue_ID}
```
