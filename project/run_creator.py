from decouple import config
from service import get_service
from gtm_creator import GTMCreator
from gtm_scanner import GTMScanner
from pprint import pprint

def create_workspace(workspace, container_path, workspace_count):
    new_workspace = gtm_creator.create_workspace(
        workspace, container_path, "TAAG_WORKSPACE", workspace_count
    )


def create_tags(workspace_path):

    script = "<script> </script>"

    html_tag_info = {"tag_name": "HTML_TAG", "tag_type": "html", "script": script}
    html_tag2_info = {"tag_name": "HTML_TAG_2", "tag_type": "html", "script": script}

    ga_pv_tag_info = {
        "tag_name": "GA_PV_TAG",
        "tag_type": "ua_pv",
        "ua_id": "UA-1234-5",
    }

    ga_pv_tag2_info = {
        "tag_name": "GA_PV_TAG_2",
        "tag_type": "ua_pv",
        "ua_id": "UA-1234-5",
    }

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

    # html_tag = gtm_creator.create_tag(workspace_path, html_tag_info)
    # html_tag = gtm_creator.create_tag(workspace_path, html_tag2_info)
    ga_pv_tag = gtm_creator.create_tag(workspace_path, ga_pv_tag_info)
    ga_pv_tag = gtm_creator.create_tag(workspace_path, ga_pv_tag2_info)
    # ga_event_tag = gtm_creator.create_tag(workspace_path, ga_event_tag_info)
    # gads_conv_tag = gtm_creator.create_tag(workspace_path, gads_conv_tag_info)
    # gads_rm_tag = gtm_creator.create_tag(workspace_path, gads_rm_tag_info)
    # flc_tag = gtm_creator.create_tag(workspace_path, flc_tag_info)
    # fls_tag = gtm_creator.create_tag(workspace_path, fls_tag_info)


def create_triggers(workspace_path):
    pv_trigger_info = {"trigger_name": "PV_TRIGGER", "trigger_type": "pageview"}
    click_trigger_info = {"trigger_name": "CLICK_TRIGGER", "trigger_type": "click"}
    click_trigger2_info = {"trigger_name": "CLICK_TRIGGER2", "trigger_type": "click"}

    pv_trigger = gtm_creator.create_trigger(workspace_path, pv_trigger_info)
    click_trigger = gtm_creator.create_trigger(workspace_path, click_trigger_info)
    click_trigger = gtm_creator.create_trigger(workspace_path, click_trigger2_info)


def create_variable(workspace_path):
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

    gtm_creator.create_variable(workspace_path, cookie_variable_info)
    gtm_creator.create_variable(workspace_path, datalayer_variable_info)
    gtm_creator.create_variable(workspace_path, cjs_variable_info)
    gtm_creator.create_variable(workspace_path, ga_settings_variable_info)


if __name__ == "__main__":

    ### SETUP ###
    CLIENT_SECRETS = config("CLIENT_SECRETS")
    ACCOUNT_ID = config("ACCOUNT_ID")
    CONTAINER_NAME = config("CONTAINER_NAME")
    CONTAINER_ID = config("CONTAINER_ID")
    WORKSPACE_NAME = config("WORKSPACE_NAME")
    WORKSPACE_ID = config("WORKSPACE_ID")

    scope = ["https://www.googleapis.com/auth/tagmanager.edit.containers"]
    service = get_service("tagmanager", "v2", scope, CLIENT_SECRETS)

    gtm_creator = GTMCreator(service)
    gtm_scanner = GTMScanner(service)

    # account = gtm_creator.get_account(ACCOUNT_ID)

    containers = gtm_creator.get_containers(ACCOUNT_ID)
    container = gtm_creator.get_container(containers, CONTAINER_NAME)
    container_path = container.get_path()

    workspaces = gtm_creator.get_workspaces(ACCOUNT_ID, CONTAINER_ID)
    workspace = gtm_creator.get_workspace(workspaces, WORKSPACE_NAME)
    workspace_count = gtm_creator.count_workspaces(workspaces)
    path = workspace.get_path()
    print(path)

    ### CREATE WORKSPACES ###
    # create_workspace(workspace, container_path, workspace_count)

    ### CREATE TAGS ###
    #create_tags(path)

    ### CREATE TRIGGERS ###
    # create_triggers(path)

    ### CREATE VARIABLES ###
    #create_variable(path)

    ### CONNECT TAG + TRIGGER ###
    scanner_workspaces = gtm_scanner.get_workspaces(ACCOUNT_ID, CONTAINER_ID)
    scanner_workspace = gtm_scanner.get_workspace(scanner_workspaces, WORKSPACE_NAME)
    scanner_ws_path = scanner_workspace.get_path()

    tag = gtm_scanner.get_tag_by_name(scanner_ws_path, 'GA_PV_TAG_2')
    trigger = gtm_scanner.get_trigger_by_name(scanner_ws_path, 'PV_TRIGGER')

    gtm_creator.connect_tag_trigger(tag, trigger)

    ### TODO 1: create version
    # gtm_creator.create_version(workspace_path)

    ### TODO 2: publish the version
    # version = GTMVersion(workspace)
    # current_version = version._version(workspace_path)

    ### TODO 3: activate all buit_in_variable & get built_in_variable

