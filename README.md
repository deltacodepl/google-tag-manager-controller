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

## Quota Limits
- 50,000 requests per project per day, which can be increased.
- 10 queries per second (QPS) per IP address
- By default, it is set to 100 requests per 100 seconds per user 
- This can be adjusted to a maximum value of 1,000. 

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

### 8. see the GTM information to run the run_scanner.py
you can see the account, container, workspace, tag, trigger, variable information by using gtm_scanner.py

```bash
python project/run_scanner.py
```

### 8. update GTM setup
you can create new workspace, tag, trigger, variable and publish by using gtm_creator.py


```bash
python project/run_creator.py
```

## Software Concept

![GitHub Logo](/images/gtm_controller.png)