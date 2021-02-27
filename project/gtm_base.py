from pprint import pprint
from account import Account
from container import Container
from workspace import Workspace


class GTMBase:
    def __init__(self, service):
        self.service = service
        self.accounts = Account(service)
        self.containers = Container(service)
        self.workspaces = Workspace(service)

    def get_accounts(self):
        return self.accounts.get_accounts()

    def get_account(self, account_id):
        self.accounts.set_account(account_id)
        return self.accounts

    def get_containers(self, account_id):
        return self.containers.get_containers(account_id)

    def get_container(self, containers, container_name):
        self.containers.set_container(containers, container_name)
        return self.containers

    def get_workspaces(self, account_id, container_id):
        return self.workspaces.get_workspaces(account_id, container_id)

    def get_workspace(self, workspace_list, workspace_name):
        self.workspaces.set_workspace(workspace_list, workspace_name)
        return self.workspaces

    def count_workspaces(self, workspaces):
        return len(workspaces["workspace"])

    def get_tag_by_name(self, workspace_path, tag_name):
        return self.workspaces.get_tag_by_name(workspace_path, tag_name)

    def get_trigger_by_name(self, workspace_path, trigger_name):
        return self.workspaces.get_trigger_by_name(workspace_path, trigger_name)

    def get_variable_by_name(self, workspace_path, variable_name):
        return self.workspaces.get_variable_by_name(workspace_path, variable_name)
