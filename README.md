<h1 align="center">Google Tag Manager Python API</h1> <br>
<h2>🐍 Table of Contents 🐍</h2>

- [About](#about)
- [Benefit](#benefit)
- [Info](#info)
- [Setup](#setup)
- [Functions](#functions)

<h2>⚡ About ⚡ </h2>
The Google Tag Manager API provides access to Google Tag Manager configuration data for an authorized user. With this API you can manage: accounts, containers, worksapces, tags, triggers and variables

## Benefit
The Google Tag Manager API handles millions of operations. To protect the system from receiving more operations than it can handle, and to ensure an equitable distribution of system resources, it is necessary to employ a quota system.

## Info
https://developers.google.com/tag-manager/api/v2/reference
https://developers.google.com/tag-manager/api/v2/devguide

## Setup
### 0. activate venv
```bash
python -m venv venv
source ./venv/bin/activate (Mac) or venv\Scripts\activate (Windows)
```

### 1. install the packages

```bash
pip install -r requirements.txt
```

### 2. create the service account in GCP for the Google Analytics API
https://console.cloud.google.com/

### 3. download the json file of the service account

### 4. create conf repository and locate client_secrets.json into this repository

```bash
mkdir conf
mv xxxxx-xxxxx.json client_secrets.json
```

### 5. create .env and put there private key and sensitive information

```bash
touch .env
```

### 6. setup the .env
- CLIENT_SECRETS='conf/client_secrets.json'
- ACCOUNT_ID='xxxx'
- CONTAINER_NAME='xxxx'
- CONTAINER_ID='xxxx'
- WORKSPACE_NAME='xxxx'
- WORKSPACE_ID='xx'

### 7. setup GTM account info

```python
CLIENT_SECRETS = config('CLIENT_SECRETS')
ACCOUNT_ID = config('ACCOUNT_ID')
CONTAINER_NAME= config('CONTAINER_NAME')
CONTAINER_ID = config('CONTAINER_ID')
WORKSPACE_NAME = config('WORKSPACE_NAME')
WORKSPACE_ID = config('WORKSPACE_ID')
```

### 8. run the main.py
```bash
python project/main.py
```


## Functions

### GTM Controller (gtm_controller.py) - Composite
- get all accounts
- print all accounts 
- get all containers
- print all containers
- get all workspaces
- print all workspaces
- get all tags
- print all tags
- get all triggers
- print all trigger
- get all variables
- print all variables

### GTM Account (account.py) - GTM-Controller Component
- get a specific account
- get the info of a account
- get the name of a account
- get the id of a account
- get the path of a account

### GTM Container (container.py) - GTM-Controller Component
- get a specific container
- get the info of a container
- get the name of a container
- get the id of a container
- get the path of a container

### GTM Workspace (workspace.py) - GTM-Controller Component
- get a specific workspace
- create an workspace
- get the info of a workspace
- get the name of a workspace
- get the id of a workspace
- get the path of a workspace
- get the container id of a workspace
- get the account id of a workspace

### GTM Tag (tag.py) - Workspace's Component
- create tag
- create html tag
- create google analytics pageview tag
- create google analytics event tag
- create google ads remarkting tag
- create google ads conversion tag
- create floodlight counter tag
- create floodlight sales tag
- get a spcific tag by the name
- connection tag and trigger
- get total info of a tag

### GTM Trigger (trigger.py) - Workspace's Component
- create a trigger
- get a spcific trigger by the name
- get total info of a tag

### GTM Variable (variable.py) - Workspace's Component
- create a variable
- get a spcific variables
- get all build-in variables

