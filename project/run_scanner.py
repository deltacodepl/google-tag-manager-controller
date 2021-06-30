from decouple import config
from service import get_service
from gtm_scanner import GTMScanner
from pprint import pprint

CLIENT_SECRETS = config("CLIENT_SECRETS")
ACCOUNT_ID = config("ACCOUNT_ID")
CONTAINER_NAME = config("CONTAINER_NAME")
CONTAINER_ID = config("CONTAINER_ID")
WORKSPACE_NAME = config("WORKSPACE_NAME")
WORKSPACE_ID = config("WORKSPACE_ID")

scope = [
    "https://www.googleapis.com/auth/tagmanager.edit.containers", 
    "https://www.googleapis.com/auth/tagmanager.delete.containers",
    "https://www.googleapis.com/auth/tagmanager.edit.containerversions",
    "https://www.googleapis.com/auth/tagmanager.publish", 
    "https://www.googleapis.com/auth/tagmanager.manage.users",
    "https://www.googleapis.com/auth/tagmanager.manage.accounts",
    ]
service = get_service("tagmanager", "v2", scope, CLIENT_SECRETS)

gtm_scanner = GTMScanner(service)


def display_all_accounts():
    accounts = gtm_scanner.get_accounts()
    gtm_scanner.print_account_list(accounts)


def display_account(account):
    gtm_scanner.print_account(account)


def display_all_containers(account_id):
    containers = gtm_scanner.get_containers(account_id)
    gtm_scanner.print_container_list(containers)


def display_container(container):
    gtm_scanner.print_container(container)


def display_all_workspaces(account_id, container_id):
    workspaces = gtm_scanner.get_workspaces(account_id, container_id)
    gtm_scanner.print_workspace_list(workspaces)


def display_workspace(workspace):
    gtm_scanner.print_workspace(workspace)


def display_gtm_overview():
    accounts = gtm_scanner.get_accounts()
    gtm_scanner.print_total_info(accounts)


if __name__ == "__main__":

    ### CALL ACCOUNT INFO ###
    # display_all_accounts()
    # account = gtm_scanner.get_account(ACCOUNT_ID)
    # display_account(account)

    ### CALL CONTAINER INFO ###
    # display_all_containers(ACCOUNT_ID)
    # containers = gtm_scanner.get_containers(ACCOUNT_ID)
    # container = gtm_scanner.get_container(containers, CONTAINER_NAME)
    # display_container(container)

    ### CALL WORKSPACE INFO ###
    # display_all_workspaces(ACCOUNT_ID, CONTAINER_ID)
    # workspaces = gtm_scanner.get_workspaces(ACCOUNT_ID, CONTAINER_ID)
    # workspace = gtm_scanner.get_workspace(workspaces, WORKSPACE_NAME)
    # workspace_path = workspace.get_path()

    ### CALL CONTAINER VERSION INFO ###
    containers = gtm_scanner.get_containers(ACCOUNT_ID)
    container = gtm_scanner.get_container(containers, CONTAINER_NAME)
    container_version = container.get_container_version()
    print(container_version)

    ### CALL GTM OVERVIEW ###
    # display_gtm_overview()

    ### CALL ALL TAGS ###
    # workspace_path = workspace.get_path()
    # print(workspace_path)
    # all_tags = gtm_scanner.get_tags(workspace_path)
    # for tag in all_tags["tag"]:
    #     gtm_scanner.print_tag_info(tag)

    ### CALL ALL TRIGGERS ###
    # workspace_path = workspace.get_path()
    # all_triggers = gtm_scanner.get_triggers(workspace_path)
    # for trigger in all_triggers["trigger"]:
    #     gtm_scanner.print_trigger_info(trigger)

    ### CALL ALL VARIABLES ###
    # workspace_path = workspace.get_path()
    # all_variables = gtm_scanner.get_variables(workspace_path)
    # for variable in all_variables["variable"]:
    #     gtm_scanner.print_variable_info(variable)

    ### CALL ALL BUILT_IN_VARIABLES ###
    # workspace_path = workspace.get_path()
    # built_in_variables = gtm_scanner.get_built_in_variables(workspace_path)
    # for built_in_val in built_in_variables["builtInVariable"]:
    #     gtm_scanner.print_built_in_variable_info(built_in_val)

    ### SELECT TAG & TRIGGER & VARIABLE ###
    # workspace_path = workspace.get_path()
    # tag = gtm_scanner.get_tag_by_name(workspace_path, 'GA_PV_TAG')
    # print(tag.get('firingTriggerId')[0])

    # trigger = gtm_scanner.get_trigger_by_name(workspace_path, 'PV_TRIGGER')
    # print(trigger.get('triggerId'))

    # variable = gtm_scanner.get_variable_by_name(workspace_path, 'COOKIE_SAMPLE')

    ### SHOW TAG & TRIGGER & VARIABLE INFO ###
    # gtm_scanner.print_tag_info(tag)
    # gtm_scanner.print_trigger_info(trigger)
    # gtm_scanner.print_variable_info(variable)
