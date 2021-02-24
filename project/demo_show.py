from decouple import config
from service import get_service
from account import Account
from container import Container
from workspace import Workspace
from gtm_controller import GTMController
from pprint import pprint

CLIENT_SECRETS = config("CLIENT_SECRETS")
ACCOUNT_ID = config("ACCOUNT_ID")
CONTAINER_NAME = config("CONTAINER_NAME")
CONTAINER_ID = config("CONTAINER_ID")
WORKSPACE_NAME = config("WORKSPACE_NAME")
WORKSPACE_ID = config("WORKSPACE_ID")

scope = ["https://www.googleapis.com/auth/tagmanager.edit.containers"]
service = get_service("tagmanager", "v2", scope, CLIENT_SECRETS)

gtm_controller = GTMController(service)

def display_gtm_overview():
    account_list = gtm_controller.get_account_list()

    for account in account_list["account"]:
        print("###### 🤖 🤖 🤖 #####")
        account_name = account['name']
        print("👻 ACCOUNT: ", account_name)
        account_id = account['accountId']

        container_list = gtm_controller.get_container_list(account_id)
        
        for container in container_list["container"]:
            container_id = container['publicId']
            print("👾 CONTAINER: ", container_id, " : ",container['name'])
            container_id = container['containerId'] 
            
            workspace_list = gtm_controller.get_workspace_list(account_id, container_id)

            for workspace in workspace_list["workspace"]:
                workspace_name = workspace['name']
                print("⚡️ WORKSPACE: ", workspace_name)


def get_acount_info():
    account_list = gtm_controller.get_account_list()
    account_info = []

    for account in account_list["account"]:
        account_name = account['name']
        account_id = account['accountId']
        container_list = gtm_controller.get_container_list(account_id)
        
        for container in container_list["container"]:
            container_id = container['publicId']
            container_id = container['containerId'] 
            
            workspace_list = gtm_controller.get_workspace_list(account_id, container_id)

            for workspace in workspace_list["workspace"]:
                workspace_name = workspace['name']
                workspace_path = workspace['path']
                
                details = {
                    'Account': account_name, 
                    'Container':container_id, 
                    'Workspace': workspace_name, 
                    'path': workspace_path,
                }

                account_info.append(details)

    return account_info

if __name__ == '__main__':
    #display_gtm_overview()
    #account_info = get_acount_info()
    #print(account_info)
    path ='accounts/6002898651/containers/38157720/workspaces/20'
    #account_info = [{'Account': 'GTM API', 'Container': '38157720', 'Workspace': 'NEW_GTM_WS', 'path': 'accounts/6002898651/containers/38157720/workspaces/23'}, {'Account': 'GTM API', 'Container': '38157720', 'Workspace': 'yuya_playing_gtm', 'path': 'accounts/6002898651/containers/38157720/workspaces/20'}, {'Account': 'GTM API', 'Container': '38157720', 'Workspace': 'Default Workspace', 'path': 'accounts/6002898651/containers/38157720/workspaces/17'}, {'Account': 'GTM API', 'Container': '40852172', 'Workspace': 'Default Workspace', 'path': 'accounts/6002898651/containers/40852172/workspaces/1'}, {'Account': 'Project X', 'Container': '34378351', 'Workspace': 'Default Workspace', 'path': 'accounts/2696165180/containers/34378351/workspaces/58'}, {'Account': 'wanamour', 'Container': '8589301', 'Workspace': 'Default Workspace', 'path': 'accounts/2696140393/containers/8589301/workspaces/242'}]
    # for a in account_info:
    #     print(a)

    #path='accounts/6002898651/containers/38157720/workspaces/20'
    #tags = gtm_controller.get_tags_with_path(path)
    #triggers = gtm_controller.get_triggers_with_path(path)
    custom_variables = gtm_controller.get_custom_variables_with_path(path)

    #gtm_controller.print_tag_list(tags)
    #gtm_controller.print_trigger_list(triggers)
    gtm_controller.print_custom_variable_list(custom_variables)


