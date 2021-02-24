from decouple import config
from service import get_service
from account import Account
from container import Container
from workspace import Workspace
from gtm_controller import GTMController

CLIENT_SECRETS = config("CLIENT_SECRETS")
ACCOUNT_ID = config("ACCOUNT_ID")
CONTAINER_NAME = config("CONTAINER_NAME")
CONTAINER_ID = config("CONTAINER_ID")
WORKSPACE_NAME = config("WORKSPACE_NAME")
WORKSPACE_ID = config("WORKSPACE_ID")

scope = ["https://www.googleapis.com/auth/tagmanager.edit.containers"]
service = get_service("tagmanager", "v2", scope, CLIENT_SECRETS)

gtm_controller = GTMController(service)

### GTM ACCOUNT ###
# account_list = gtm_controller.get_account_list()
# gtm_controller.print_account_list(account_list)
account1 = gtm_controller.get_account(ACCOUNT_ID)
account_path = account1._path()

### GTM CONTAINER ###
# container_list = gtm_controller.get_container_list(ACCOUNT_ID)
# gtm_controller.print_container_list(container_list)
container1 = gtm_controller.get_container(account_path, CONTAINER_NAME)
container_path = container1._path()

### GTM WORKSPACE ###
# workspace_list = gtm_controller.get_workspace_list(ACCOUNT_ID, CONTAINER_ID)
# gtm_controller.print_workspace_list(workspace_list)
workspace1 = gtm_controller.get_workspace(container_path, WORKSPACE_NAME)
workspace_path = workspace1._path()
# workspace_count = gtm_controller.count_workspace(workspace_list)
# new_workspace = gtm_controller.create_workspace(container_path, 'NEW_GTM_WS', workspace_count)


### GTM TAG ###
# tag_list = gtm_controller.get_tag_list(ACCOUNT_ID, CONTAINER_ID, WORKSPACE_ID)
# gtm_controller.print_tag_list(tag_list)

script = "<script>....</script>"

html_tag_info = {"tag_name": "HTML_TAG", "tag_type": "html", "script": script}

ga_pv_tag_info = {"tag_name": "GA_PV_TAG", "tag_type": "ua_pv", "ua_id": "UA-1234-5"}

ga_event_tag_info = {
    "tag_name": "GA_EVENT_TAG",
    "tag_type": "ua_event",
    "ua_id": "UA-1234-5",
    "ga_settings": "{{Google Analytics settings}}",
    "non_interaction": "false",
    "event_category": "ec-y",
    "event_action": "ea-y",
    "event_label": "el-yy",
}

gads_conv_tag_info = {
    "tag_name": "GADS_CONV_TAG",
    "tag_type": "awct",
    "conv_id": "12345",
    "conv_label": "label1123",
}
gads_rm_tag_info = {
    "tag_name": "GADS_RM_TAG",
    "tag_type": "sp",
    "conv_id": "12345",
    "conv_label": "label1123",
}

flc_tag_info = {
    "tag_name": "FLOODLIGHT_COUNT_TAG",
    "tag_type": "flc",
    "advertiser_id": "555",
    "group_tag": "666",
    "activity_tag": "2222",
    "count_method": "STANDARD",
}
fls_tag_info = {
    "tag_name": "FLOODLIGHT_SALES_TAG2",
    "tag_type": "fls",
    "advertiser_id": "555",
    "group_tag": "666",
    "activity_tag": "2222",
    "count_method": "TRANSACTIONS",
    "revenue": "1000",
    "order_id": "id-yyyy",
}


# html_tag = workspace1.create_tag(workspace_path, html_tag_info)
# ga_pv_tag = workspace1.create_tag(workspace_path, ga_pv_tag_info)
# ga_event_tag = workspace1.create_tag(workspace_path, ga_event_tag_info)
# gads_conv_tag = workspace1.create_tag(workspace_path, gads_conv_tag_info)
# gads_rm_tag = workspace1.create_tag(workspace_path, gads_rm_tag_info)
# flc_tag = workspace1.create_tag(workspace_path, flc_tag_info)
# fls_tag = workspace1.create_tag(workspace_path, fls_tag_info)


### GTM TRIGGER ###
# trigger_list = gtm_controller.get_trigger_list(ACCOUNT_ID, CONTAINER_ID, WORKSPACE_ID)
# gtm_controller.print_trigger_list(trigger_list)

pv_trigger_info = {"trigger_name": "PV_TRIGGER", "trigger_type": "pageview"}
click_trigger_info = {"trigger_name": "CLICK_TRIGGER", "trigger_type": "click"}

# pv_trigger = workspace1.create_trigger(workspace_path, pv_trigger_info)
# click_trigger = workspace1.create_trigger(workspace_path, click_trigger_info)

### GTM TAG + TRIGGER CONNECT ###
# fls_tag = workspace1.get_tag_by_name(workspace_path, 'FLOODLIGHT_SALES_TAG2')
# workspace1.tag_info(fls_tag)
# click_trigger = workspace1.get_trigger_by_name(workspace_path, 'CLICK_TRIGGER')
# workspace1.trigger_info(click_trigger)
# workspace1.connect_tag_trigger(fls_tag, click_trigger)


### GTM VARIABLE ###
# custom_variable_list = gtm_controller.get_custom_variable_list(ACCOUNT_ID, CONTAINER_ID, WORKSPACE_ID)
# gtm_controller.print_custom_variable_list(custom_variable_list)
script = 'function(){\n  return console.log("heyo")\n}'

datalayer_variable_info = {
    "name": "DLV_SAMPLE",
    "type": "v",
    "value": "datalayer-name",
    "param_key": "name",
}
cookie_variable_info = {
    "name": "COOKIE_SAMPLE",
    "type": "k",
    "value": "demo-cookie",
    "param_key": "name",
}
cjs_variable_info = {
    "name": "CUSTOM_JS",
    "type": "jsm",
    "value": script,
    "param_key": "javascript",
}
ga_settings_variable_info = {
    "name": "GA_SETTINGS",
    "type": "gas",
    "value": "UA-1234-5",
    "param_key": "trackingId",
}

# workspace1.create_variable(workspace_path, cookie_variable_info)
# workspace1.create_variable(workspace_path, datalayer_variable_info)
# workspace1.create_variable(workspace_path, cjs_variable_info)
# workspace1.create_variable(workspace_path, ga_settings_variable_info)

# ga_settings = workspace1.get_variable_by_name(workspace_path, 'Google Analytics settings')
# workspace1.variable_info(ga_settings)


### GTM BUILT_IN_VARIABLE ###
# built_in_variable_list = gtm_controller.get_built_in_variable_list(ACCOUNT_ID, CONTAINER_ID, WORKSPACE_ID)
# gtm_controller.print_built_in_variable_list(built_in_variable_list)

### TODO 3: activate all buit_in_variable & get built_in_variable


### TODO 1: create version
# workspace._create_version(workspace_path)


## TODO 2: publish the version
# version = GTMVersion(workspace)
# current_version = version._version(workspace_path)
