import time
from time import sleep, gmtime

from decouple import config
from service import get_service
from gtm_creator import GTMCreator
from gtm_scanner import GTMScanner
from pprint import pprint
from sheets import setup, get_listed_values
import json


def create_workspace(workspace, container_path, workspace_count):
    new_workspace = gtm_creator.create_workspace(
        workspace, container_path, "TAAG_WORKSPACE", workspace_count
    )


def create_tags(workspace_path):
    script = "<script>\nfunction getSelectionText() {" \
             "var text = '';" \
             "if'(window.getSelection) {" \
             "text = window.getSelection().toString();" \
             "} else if (document.selection && document.selection.type != 'Control') {" \
             "text = document.selection.createRange().text;}" \
             "return text;}", \
        "document.addEventListener(\"copy\", function(e){" \
        "dataLayer.push({" \
        "'event': 'textCopied'," \
        "'clipboardText': getSelectionText()," \
        "'clipboardLength': getSelectionText().length }); });</script>"


    script2 = "<script>\n// Declare function to get selected text from document\nfunction getSelectionText() {\nvar text = '';\nif (window.getSelection) {\ntext = window.getSelection().toString();\n} else if (document.selection && document.selection.type != 'Control') {\ntext = document.selection.createRange().text;\n}\nreturn text;\n}\n\n// Declare function on copy event\ndocument.addEventListener(\"copy\", function(e){\ndataLayer.push({\n'event': 'textCopied',\n'clipboardText': getSelectionText(),\n'clipboardLength': getSelectionText().length\n});\n});\n</script>"

    html_tag_info = {"tag_name": "HTML_TAG", "tag_type": "html", "script": script}
    html_tag2_info = {"tag_name": "HTML_COPY_TAG", "tag_type": "html", "script": script2}

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

    main_tag_info = {
        "tag_name": "GA4_tapflo.ca",
        "tag_type": "googtag",
        "tag_id": TAG_ID
    }

    ga_copy_mail_tag_info = {
        "tag_name": "GA4_copy_mail",
        "tag_type": "gaawe",
        "tag_id": TAG_ID,
    }
    ga_copy_tel_tag_info = {
        "tag_name": "GA4_copy_tel",
        "tag_type": "gaawe",
        "tag_id": TAG_ID,
    }
    ga_click_mail_tag_info = {
        "tag_name": "GA4_click_mail",
        "tag_type": "gaawe",
        "tag_id": TAG_ID,
    }
    ga_click_tel_tag_info = {
        "tag_name": "GA4_click_tel",
        "tag_type": "gaawe",
        "tag_id": TAG_ID,
    }


    gads_conv_tag_info = {
        "tag_name": "GADS_CONV_TAG",
        "tag_type": "awct",
        "conv_id": "",
        "conv_label": "GAD_conv",
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
    print("👾 Creating Tags")
    # html_tag = gtm_creator.create_tag(workspace_path, html_tag_info)
    if not gtm_creator.get_tag_by_name(workspace_path, html_tag2_info["tag_name"]):
        html_tag = gtm_creator.create_tag(workspace_path, html_tag2_info)
    # ga_pv_tag = gtm_creator.create_tag(workspace_path, ga_pv_tag_info)
    if not gtm_creator.get_tag_by_name(workspace_path, ga_copy_tel_tag_info["tag_name"]):
        ga_event_tag = gtm_creator.create_tag(workspace_path, ga_copy_tel_tag_info)
    if not gtm_creator.get_tag_by_name(workspace_path, ga_copy_mail_tag_info.get("tag_name")):
        ga_copy_mail_tag = gtm_creator.create_tag(workspace_path, ga_copy_mail_tag_info)
    if not gtm_creator.get_tag_by_name(workspace_path, ga_click_mail_tag_info.get("tag_name")):
        ga_click_mail_tag = gtm_creator.create_tag(workspace_path, ga_click_mail_tag_info)
    if not gtm_creator.get_tag_by_name(workspace_path, ga_click_tel_tag_info.get("tag_name")):
        gtm_creator.create_tag(workspace_path, ga_click_tel_tag_info)
        sleep(5)

    if not gtm_creator.get_tag_by_name(workspace_path, main_tag_info.get("tag_name")):
        main_tag = gtm_creator.create_tag(workspace_path, main_tag_info)


    # Google Ads Tag
    # gads_conv_tag = gtm_creator.create_tag(workspace_path, gads_conv_tag_info)
    # gads_rm_tag = gtm_creator.create_tag(workspace_path, gads_rm_tag_info)
    # flc_tag = gtm_creator.create_tag(workspace_path, flc_tag_info)
    # fls_tag = gtm_creator.create_tag(workspace_path, fls_tag_info)
    time.sleep(10)

def create_tags_sheet(workspace_path, tags):
    for tag in tags:
        tag_type = tag[1]
        tag_name = tag[2]
        details = tag[3]

        if tag_type == 'ua_pv':
            tag_info = {"tag_name": tag_name, "tag_type": tag_type, "ua_id": details}
            ga_pv_tag = gtm_creator.create_tag(workspace_path, tag_info)

        elif tag_type == 'awct':
            conv_id, conv_label = details.split('|')
            tag_info = {"tag_name": tag_name, "tag_type": tag_type, "conv_id": conv_id, "conv_label": conv_label}
            gads_conv_tag = gtm_creator.create_tag(workspace_path, tag_info)

        elif tag_type == 'html':
            tag_info = {"tag_name": tag_name, "tag_type": tag_type, "script": details}
            html_tag = gtm_creator.create_tag(workspace_path, tag_info)

        else:
            tag_info = None


def create_triggers_sheets(workspace_path, triggers):
    # TODO:
    pass


def create_triggers(workspace_path):
    pv_trigger_info = {"trigger_name": "PV_TRIGGER", "trigger_type": "pageview"}
    click_trigger_info = {"trigger_name": "CLICK_TRIGGER", "trigger_type": "click"}
    click_trigger2_info = {"trigger_name": "CLICK_TRIGGER2", "trigger_type": "click"}

    page_path_trigger_info = {"trigger_name": "show_thx_page", "trigger_type": "PAGEVIEW", "tag_id": TAG_ID}
    copy_tel_trigger_info = {"trigger_name": "copy_tel", "trigger_type": "CUSTOM_EVENT", "tag_id": TAG_ID}
    copy_mail_trigger_info = {"trigger_name": "copy_mail", "trigger_type": "CUSTOM_EVENT", "tag_id": TAG_ID}
    click_mail_trigger_info = {"trigger_name": "click_mail", "trigger_type": "CLICK", "tag_id": TAG_ID}
    click_tel_trigger_info = {"trigger_name": "click_tel", "trigger_type": "CLICK", "tag_id": TAG_ID}
    dom_ready_trigger_info = {"trigger_name": "dom_ready", "trigger_type": "DOM_READY", "tag_id": TAG_ID}

    copy_tel_filters = {
        "customEventFilter": [
            {
                "type": "EQUALS",
                "parameter": [
                    {
                        "type": "TEMPLATE",
                        "key": "arg0",
                        "value": "{{_event}}"
                    },
                    {
                        "type": "TEMPLATE",
                        "key": "arg1",
                        "value": "textCopied"
                    }
                ]
            }
        ],
        "filter": [
            {
                "type": "CONTAINS",
                "parameter": [
                    {
                        "type": "TEMPLATE",
                        "key": "arg0",
                        "value": "{{DLV_COPY}}"
                    },
                    {
                        "type": "TEMPLATE",
                        "key": "arg1",
                        "value": "727"
                    }
                ]
            }
        ],
    }
    copy_mail_filters = {
        "customEventFilter": [
            {
                "type": "EQUALS",
                "parameter": [
                    {
                        "type": "TEMPLATE",
                        "key": "arg0",
                        "value": "{{_event}}"
                    },
                    {
                        "type": "TEMPLATE",
                        "key": "arg1",
                        "value": "textCopied"
                    }
                ]
            }
        ],
        "filter": [
            {
                "type": "CONTAINS",
                "parameter": [
                    {
                        "type": "TEMPLATE",
                        "key": "arg0",
                        "value": "{{DLV_COPY}}"
                    },
                    {
                        "type": "TEMPLATE",
                        "key": "arg1",
                        "value": "@tapflo"
                    }
                ]
            }
        ],
    }
    click_mail_filters = {
        "filter": [
            {
                "type": "CONTAINS",
                "parameter": [
                    {
                        "type": "TEMPLATE",
                        "key": "arg0",
                        "value": "{{Click URL}}"
                    },
                    {
                        "type": "TEMPLATE",
                        "key": "arg1",
                        "value": "mailto:"
                    }
                ]
            }
        ]
    }
    click_tel_filters = {
        "filter": [
            {
                "type": "CONTAINS",
                "parameter": [
                    {
                        "type": "TEMPLATE",
                        "key": "arg0",
                        "value": "{{Click URL}}"
                    },
                    {
                        "type": "TEMPLATE",
                        "key": "arg1",
                        "value": "tel:"
                    }
                ]
            }
        ]
    }
    page_path_filters = {
        "filter": [
            {
                "type": "CONTAINS",
                "parameter": [
                    {
                        "type": "TEMPLATE",
                        "key": "arg0",
                        "value": "{{Page Path}}"
                    },
                    {
                        "type": "TEMPLATE",
                        "key": "arg1",
                        "value": "dziekuje"
                    }
                ]
            },
            {
                "type": "CONTAINS",
                "parameter": [
                    {
                        "type": "TEMPLATE",
                        "key": "arg0",
                        "value": "{{Referrer}}"
                    },
                    {
                        "type": "TEMPLATE",
                        "key": "arg1",
                        "value": "tapflo.com.pl"
                    }
                ]
            }
        ],
    }
    # pv_trigger = gtm_creator.create_trigger(workspace_path, pv_trigger_info)
    # click_trigger = gtm_creator.create_trigger(workspace_path, click_trigger_info)
    # click_trigger = gtm_creator.create_trigger(workspace_path, click_trigger2_info)
    if not gtm_creator.get_trigger_by_name(workspace_path, page_path_trigger_info.get("trigger_name")):
        page_path_trigger = gtm_creator.create_trigger(workspace_path, page_path_trigger_info, page_path_filters)
        print(page_path_trigger)

    if not gtm_creator.get_trigger_by_name(workspace_path, copy_tel_trigger_info.get("trigger_name")):
        copy_tel_trigger = gtm_creator.create_trigger(workspace_path, copy_tel_trigger_info, copy_tel_filters)
    if not gtm_creator.get_trigger_by_name(workspace_path, copy_mail_trigger_info.get("trigger_name")):
        copy_mail_trigger = gtm_creator.create_trigger(workspace_path, copy_mail_trigger_info, copy_mail_filters)
    if not gtm_creator.get_trigger_by_name(workspace_path, click_mail_trigger_info.get("trigger_name")):
        click_mail_trigger = gtm_creator.create_trigger(workspace_path, click_mail_trigger_info, click_mail_filters)
        if not gtm_creator.get_trigger_by_name(workspace_path, click_tel_trigger_info.get("trigger_name")):
            click_tel_trigger = gtm_creator.create_trigger(workspace_path, click_tel_trigger_info, click_tel_filters)
    if not gtm_creator.get_trigger_by_name(workspace_path, dom_ready_trigger_info.get("trigger_name")):
        dom_ready_trigger = gtm_creator.create_trigger(workspace_path, dom_ready_trigger_info, {})

def create_variable(workspace_path):
    script = 'function(){\n  return console.log("heyo")\n}'

    datalayer_variable_info = {
        "name": "DLV_COPY",
        "type": "v",
        "value": "2",
        "param_key": "dataLayerVersion",
    }
    datalayer_variable_info_2 = {
        "name": "DLV_COPY",
        "type": "v",
        "value": "clipboardText",
        "param_key": "name",
    }
    click_url_variable_info = {
        "type": "CLICK_URL",
        "name": "Click URL"
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
    print("👾 Creating Variables...")
    # gtm_creator.create_variable(workspace_path, cookie_variable_info)
    # gtm_creator.create_variable(workspace_path, datalayer_variable_info)
    if not gtm_creator.get_variable_by_name(workspace_path, "DLV_COPY"):
        gtm_creator.create_variable(workspace_path, datalayer_variable_info_2)
    gtm_creator.create_builtin_variable(workspace_path)

    # if not gtm_creator.get_variable_by_name(workspace_path, "Click URL"):
    #     gtm_creator.create_variable(workspace_path, click_url_variable_info)
    # gtm_creator.create_variable(workspace_path, cjs_variable_info)
    # gtm_creator.create_variable(workspace_path, ga_settings_variable_info)


def read_tags_from_sheets():
    sheets_id = '1YdfQ7darmZCJCAJLOCVDGzfAI4BXxPijCus_ZH_ws9Y'  # Part_Of_Google_Sheets_URL
    tab = 'tags!A1:G50'
    sheet = setup(sheets_id)
    result = get_listed_values(sheets_id, sheet, tab)
    return result


def read_triggers_from_sheets():
    sheets_id = '17Nu32XCIIENCtmQRx9olx5R0dh4eb6CRuP99ik1d3hk'  # Part_Of_Google_Sheets_URL
    tab = 'trigger!A1:G50'
    sheet = setup(sheets_id)
    result = get_listed_values(sheets_id, sheet, tab)
    return result


if __name__ == "__main__":
    ### SETUP ###
    CLIENT_SECRETS = config("CLIENT_SECRETS")
    ACCOUNT_ID = config("ACCOUNT_ID")
    CONTAINER_NAME = config("CONTAINER_NAME")
    CONTAINER_ID = config("CONTAINER_ID")
    WORKSPACE_NAME = config("WORKSPACE_NAME")
    WORKSPACE_ID = config("WORKSPACE_ID")
    TAG_ID = config("TAG_ID")

    scope = ["https://www.googleapis.com/auth/tagmanager.edit.containers"]
    service = get_service("tagmanager", "v2", scope, CLIENT_SECRETS)

    gtm_creator = GTMCreator(service)
    gtm_scanner = GTMScanner(service)

    # account = gtm_creator.get_account(ACCOUNT_ID)

    # containers = gtm_creator.get_containers(ACCOUNT_ID)
    # container = gtm_creator.get_container(containers, CONTAINER_NAME)
    # container_path = container.get_path()

    workspaces = gtm_creator.get_workspaces(ACCOUNT_ID, CONTAINER_ID)
    workspace = gtm_creator.get_workspace(workspaces, WORKSPACE_NAME)
    workspace_path = workspace.get_path()
    print(workspace_path)

    tags = read_tags_from_sheets()
    print(tags)
    # create_tags_sheet(workspace_path, tags)

    # trigger = read_triggers_from_sheets()
    # print(trigger)

    ### CREATE WORKSPACES ###
    # create_workspace(workspace, container_path, workspace_count)

    ### CREATE TAGS ###
    # create_tags(workspace_path)
    create_tags(workspace_path)
    ### CREATE TRIGGERS ###
    create_triggers(workspace_path)

    ### CREATE VARIABLES ###
    create_variable(workspace_path)

    ### CONNECT TAG + TRIGGER ###
    tag_triggers_dict = {
        'GA4_copy_tel': 'copy_tel',
        'GA4_copy_mail': 'copy_mail',
        'GA4_click_tel': 'click_tel',
        'GA4_click_mail': 'click_mail',
        #'GA4_contact_form': 'show_thx_page',
        'HTML_COPY_TAG': 'dom_ready',
    }
    # all_tags = gtm_scanner.get_tags(workspace_path)
    # for tag in all_tags["tag"]:
    print("Resolving workspaces...")
    sleep(10)
    scanner_workspaces = gtm_scanner.get_workspaces(ACCOUNT_ID, CONTAINER_ID)
    scanner_workspace = gtm_scanner.get_workspace(scanner_workspaces, WORKSPACE_NAME)
    scanner_ws_path = scanner_workspace.get_path()
    print("Connecting triggers...")
    sleep(20)
    for key, value in tag_triggers_dict.items():
        sleep(20)
        print(key, value)
        gtm_creator.connect_tag_trigger(gtm_scanner.get_tag_by_name(scanner_ws_path, key),
                                                                    gtm_scanner.get_trigger_by_name(scanner_ws_path, value))

    print(f"👾 Triggers connected... {tag_triggers_dict}")

    ### TODO 1: create version
    ### CREATE & READ GTM Container Version ###
    containers = gtm_scanner.get_containers(ACCOUNT_ID)
    container = gtm_scanner.get_container(containers, CONTAINER_NAME)
    container_version = container.get_container_version()

    print(dir(container_version))
    # new_container_version = gtm_creator.create_version(workspace_path, container_version, 'yt version x', 'this is some notes')
    # print(new_container_version)

    # TODO 1#
    ### Publish the Container Version ###

    ### TODO 2: publish the version
    # version = GTMVersion(workspace)
    # current_version = version._version(workspace_path)

    ### TODO 3: activate all buit_in_variable & get built_in_variable
