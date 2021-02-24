from pprint import pprint
from account import Account
from container import Container
from workspace import Workspace


class GTMController:
    def __init__(self, service):
        self.service = service
        self.accounts = self.service.accounts()
        self.containers = self.service.accounts().containers()
        self.workspaces = self.service.accounts().containers().workspaces()

    def get_account(self, account_id):
        self.account = Account(self.accounts, account_id)
        return self.account

    def get_account_list(self):
        return self.accounts.list().execute()

    def print_account_list(self, account_list):
        for account in account_list["account"]:
            print("### account ###")
            pprint(account)

    def get_container(self, account_path, container_name):
        self.container = Container(account_path, self.containers, container_name)
        return self.container

    def get_container_list(self, account_id):
        self.account_path = f"accounts/{account_id}"
        return self.containers.list(parent=self.account_path).execute()

    def print_container_list(self, container_list):
        for container in container_list["container"]:
            print("### container ###")
            pprint(container)

    def get_workspace(self, container_path, workspace_name):
        self.workspace = Workspace(container_path, self.workspaces, workspace_name)
        return self.workspace

    def get_workspace_list(self, account_id, container_id):
        path = f"accounts/{account_id}/containers/{container_id}"
        workspaces = self.workspaces.list(parent=path).execute()
        return workspaces

    def print_workspace_list(self, workspace_list):
        for workspace in workspace_list["workspace"]:
            print("### workspace ###")
            pprint(workspace)

    def count_workspace(self, workspace_list):
        return len(workspace_list["workspace"])

    def create_workspace(self, container_path, workspace_name, workspace_count):
        new_workspace = self.workspace.create_workspace(
            container_path, self.workspaces, workspace_name, workspace_count
        )
        return new_workspace

    def get_tag_list(self, account_id, container_id, workspace_id):
        path = (
            f"accounts/{account_id}/containers/{container_id}/workspaces/{workspace_id}"
        )
        tags = self.workspaces.tags().list(parent=path).execute()
        return tags

    def get_tags_with_path(self, path):
        tags = self.workspaces.tags().list(parent=path).execute()
        return tags 

    def print_tag_list(self, tags):
        for tag in tags["tag"]:
            print("##### 🤖  TAG 🤖 #####")
            print("👻 TAG: ", tag['name'])
            print("👾 TAG ID: ", tag['tagId'])
            print("⚡️ DETAILS: ")
            pprint(tag)

    def get_trigger_list(self, account_id, container_id, workspace_id):
        path = (
            f"accounts/{account_id}/containers/{container_id}/workspaces/{workspace_id}"
        )
        triggers = self.workspaces.triggers().list(parent=path).execute()
        return triggers

    def get_triggers_with_path(self, path):
        triggers = self.workspaces.triggers().list(parent=path).execute()
        return triggers

    def print_trigger_list(self, triggers):
        for trigger in triggers["trigger"]:
            print("##### 🤖  TRIGGER 🤖 #####")
            print("👻 TRIGGER: ", trigger['name'])
            print("👾 TRIGGER ID: ", trigger['triggerId'])
            print("⚡️ DETAILS: ")
            pprint(trigger)

    def get_custom_variable_list(self, account_id, container_id, workspace_id):
        path = (
            f"accounts/{account_id}/containers/{container_id}/workspaces/{workspace_id}"
        )
        custom_variables = self.workspaces.variables().list(parent=path).execute()

        return custom_variables

    def print_custom_variable_list(self, custom_variables):
        for variable in custom_variables["variable"]:

            print("##### 🤖 CUSTOM VARIABLE 🤖 #####")
            print("👻 VARIABLE: ", variable['name'])
            print("👾 VARIABLE ID: ", variable['variableId'])
            print("⚡️ DETAILS: ")
            pprint(variable)

    def get_custom_variables_with_path(self, path):
        custom_variables = self.workspaces.variables().list(parent=path).execute()
        return custom_variables

    def get_built_in_variable_list(self, account_id, container_id, workspace_id):
        path = (
            f"accounts/{account_id}/containers/{container_id}/workspaces/{workspace_id}"
        )
        built_in_variables = (
            self.workspaces.built_in_variables().list(parent=path).execute()
        )

        return built_in_variables

    def print_built_in_variable_list(self, built_in_variables):
        for variable in built_in_variables["builtInVariable"]:
            print("### builtInVariable ###")
            pprint(variable)

    # def _create_version(self, workspace_path):
    #     request = self.workspaces.create_version(
    #             path=workspace_path, body={"name": 'name', "notes": 'notes'})
    #     response = request.execute()
    #     version = response.workspaces.get("containerVersion")

    #     print(version)
