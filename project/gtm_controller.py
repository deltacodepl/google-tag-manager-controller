from pprint import pprint

class GTMController():

    def __init__(self, service): 
        if service.accounts().containers():
            self.accounts = service.accounts()
            self.containers = service.accounts().containers()
            self.workspaces = service.accounts().containers().workspaces()
        else:
            print("Container not exist")

    def get_account_list(self):
        return self.accounts.list().execute()

    def print_account_list(self, account_list):
        for account in account_list['account']:
            print('### account ###')
            pprint(account)

    def get_container_list(self, account_id):
        path = f'accounts/{account_id}'
        return self.containers.list(parent=path).execute()

    def print_container_list(self, container_list):
        for container in container_list['container']:
            print('### container ###')
            pprint(container)

    def get_workspace_list(self, account_id, container_id):
        path = f'accounts/{account_id}/containers/{container_id}'
        workspaces = self.workspaces.list(parent=path).execute()
        return workspaces

    def print_workspace_list(self, workspace_list):
        for workspace in workspace_list['workspace']:
            print('### workspace ###')
            pprint(workspace)

    def count_workspace(self, workspace_list):
        return len(workspace_list['workspace'])

    def get_tag_list(self, account_id, container_id, workspace_id):
        path = f'accounts/{account_id}/containers/{container_id}/workspaces/{workspace_id}'
        tags = self.workspaces.tags().list(parent=path).execute()

        return tags
    
    def print_tag_list(self, tags):
        for tag in tags['tag']:
            print('### tag ###')
            pprint(tag)

    def get_trigger_list(self, account_id, container_id, workspace_id):
        path = f'accounts/{account_id}/containers/{container_id}/workspaces/{workspace_id}'
        triggers = self.workspaces.triggers().list(parent=path).execute()

        return triggers
    
    def print_trigger_list(self, triggers):
        for trigger in triggers['trigger']:
            print('### trigger ###')
            pprint(trigger)

    def get_custom_variable_list(self, account_id, container_id, workspace_id):
        path = f'accounts/{account_id}/containers/{container_id}/workspaces/{workspace_id}'
        custom_variables = self.workspaces.variables().list(parent=path).execute()

        return custom_variables
    
    def print_custom_variable_list(self, custom_variables):
        for variable in custom_variables['variable']:
            print('### custom variable ###')
            pprint(variable)

    def get_built_in_variable_list(self, account_id, container_id, workspace_id):
        path = f'accounts/{account_id}/containers/{container_id}/workspaces/{workspace_id}'
        built_in_variables = self.workspaces.built_in_variables().list(parent=path).execute()

        return built_in_variables
    
    def print_built_in_variable_list(self, built_in_variables):
        for variable in built_in_variables['builtInVariable']:
            print('### builtInVariable ###')
            pprint(variable)

