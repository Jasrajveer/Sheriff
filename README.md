# Updates
3-12-26
Explicit error handling update. Previously was slilently printing errors.
Improved reliability when using Sheriff for in-service or non-interactive environments.
Fixed Jira file attachment flow. Ensuring ticket creation before file upload attempt.
Included config file parsing check.

# Sheriff
Sheriff is a Python incident automation tool that can create Jira tickets, write local incident logs, and send email notifications from a single command.
It is designed for teams that want a lightweight way to route incidents to multiple outputs (e.g., Jira + log file) using a config-driven workflow.

## Features
- **Jira support** for both Jira Cloud and Jira Server.
- **Local JSON log output** for incident recordkeeping.
- **Email notifications** using configured recipient lists.
- **Config-driven routing**: execute one or more target groups in the same run.
- **CLI and Python API support**.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Configuration](#configuration)
- [Usage](#usage)
  - [CLI](#cli)
  - [Python API](#python-api)
- [Output and Behavior](#output-and-behavior)
- [Troubleshooting](#troubleshooting)
- [Security Notes](#security-notes)

---

## Requirements

- Python **3.7+** (project metadata currently requires >3.6).
- Access to your Jira instance (Cloud or Server), if using Jira target groups.
- A valid YAML configuration file.

---

## Installation

From the repository root:
```bash
pip install .
```

Optional (recommended):
```bash
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install .
```

---

## Quick Start

1. Create/update your `config.yml`.
2. Run Sheriff with summary, description, config path, and one or more groups:
```bash
incidents \
  -s "Build pipeline failure" \
  -d "Deployment failed in stage prod-us-east-1" \
  -c ./config.yml \
  -p jira_project mnt-issue_log
```

---

## Configuration

Sheriff uses a YAML file with named groups. Each group has a `type` (for example `jira` or `log_file`) and the fields required by that type.

---

## Usage

### CLI

```
incidents -h
```

Expected options:

- `-s, --summary` (required): short incident summary.
- `-d, --description` (optional): incident details.
- `-c, --config` (required): path to YAML config.
- `-u, --upload_file` (optional): file attachment for Jira issues.
- `-p, --project_name` (required, one or many): config group names.

### Python API

```python
from incidents.controller import Controller

Controller(
    config="/path/to/config.yml",
    summary="API example incident",
    description="Triggered from a Python script",
    groups=["jira_project", "mnt-issue_log"],
    upload=None,
).load_platform()
```

---

## Output and Behavior

Depending on configured groups, Sheriff can:

- create a Jira ticket,
- append a JSON record to a local log file,
- send an email notification,
- update statistics data.

If one or more platform actions fail, errors are surfaced to help calling scripts/automation detect failure.

---

## Troubleshooting

- **`ModuleNotFoundError`** for dependencies:
  - Ensure you installed the package in the active Python environment.
- **Config parsing errors**:
  - Validate YAML format and required keys for the selected group type.
- **Jira authentication failures**:
  - Verify host URL, user, and API token/password values.
- **Email issues**:
  - Validate recipient list sources and local mail command availability.

---

## Security Notes
- New security method will be implemented in next updates.
- Do **not** commit credentials (API keys/passwords) to source control.
- Prefer environment-specific config management (secrets manager, CI variables, etc.).
- Restrict access to config files containing authentication details.

