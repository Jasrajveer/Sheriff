"""The general idea for this tool is to have a quick way to create an issue/ticket on one or more
incident tracking platforms, using the command line.The program currently has two main functions,
read the config file, and based on what is specified create issues to track. The config file
contains the platforms and the complementary information based on what needs to be specified for
that platform. There are options including summary, description, and component, which are needed
for creating the issue."""
import argparse
import sys
from incidents.controller import Controller

def main():
    """Pass all the options to parse_config.py. These options will be coupled with the incident tracking components specified in the config file."""
    parser = argparse.ArgumentParser(description='Gather all information for creating a ticket.')
    parser.add_argument('-d', '--description', help='Description of the failure/error.')
    parser.add_argument('-s', '--summary', required=True, help='Summary for the issue/ticket.')
    parser.add_argument('-c', '--config', required=True, help='Path to config file.')
    parser.add_argument('-u', '--upload_file', help='Path to file for uploading to jira ticket.')
    parser.add_argument('-p', '--project_name', nargs='+',required=True, help='Project name for preset information in Config.')
    args = parser.parse_args()

    try:
        Controller(config=args.config, description=args.description, summary=args.summary,
        upload=args.upload_file, groups=args.project_name).load_platform()
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
