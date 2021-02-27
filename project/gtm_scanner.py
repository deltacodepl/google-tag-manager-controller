from pprint import pprint
from gtm_base import GTMBase

class GTMScanner(GTMBase):
    def __init__(self, service):
        super().__init__(service)

    def print_account_list(self, account_list):
        for num, account in enumerate(account_list["account"]):
            print(num, "🤖 ACCOUNT")
            print("👾 NAME: ", account["name"])
            print("👾 ID: ", account["accountId"], "\n")

    def print_account(self, account):
        print("🤖 ACCOUNT")
        print("👾 NAME: ", account.get_name())
        print("👾 ID: ", account.get_id())
        print("👾 PATH: ", account.get_path())

    def print_container_list(self, container_list):
        for num, container in enumerate(container_list["container"]):
            print(num, "🤖 CONTAINER")
            print("👾 ID: ", container["publicId"])
            print("👾 NAME: ", container["name"], "\n")

    def print_container(self, container):
        print("🤖 CONTAINER")
        print("👾 NAME: ", container.get_name())
        print("👾 ID: ", container.get_id())
        print("👾 PATH: ", container.get_path())

    def print_workspace_list(self, workspace_list):
        for num, workspace in enumerate(workspace_list["workspace"]):
            print(num, "🤖 WORKSPACE")
            print("👾 ID: ", workspace["workspaceId"])
            print("👾 NAME: ", workspace["name"], "\n")

    def print_workspace(self, workspace):
        print("🤖 WORKSPACE")
        print("👾 NAME: ", workspace.get_name())
        print("👾 ID: ", workspace.get_id())
        print("👾 PATH: ", workspace.get_path())

    def print_total_info(self, account_list):
        for account in account_list["account"]:
            print("###### 🤖 🤖 🤖 #####")
            account_name = account["name"]
            print("👻 ACCOUNT: ", account_name)
            account_id = account["accountId"]

            container_list = self.get_containers(account_id)

            for container in container_list["container"]:
                container_id = container["publicId"]
                print("👾 CONTAINER: ", container_id, " : ", container["name"])
                container_id = container["containerId"]

                workspace_list = self.get_workspaces(account_id, container_id)

                for workspace in workspace_list["workspace"]:
                    workspace_name = workspace["name"]
                    print("⚡️ WORKSPACE: ", workspace_name)

    def print_tag_info(self, tag):
        self.workspaces.print_tag_info(tag)

    def print_trigger_info(self, trigger):
        self.workspaces.print_trigger_info(trigger)

    def print_variable_info(self, variable):
        self.workspaces.print_variable_info(variable)
