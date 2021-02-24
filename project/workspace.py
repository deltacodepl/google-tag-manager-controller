from pprint import pprint
from container import Container
from tag import Tag
from trigger import Trigger
from variable import Variable


class Workspace(Container):
    def __init__(self, container_path, workspaces, workspace_name):

        request = workspaces.list(parent=container_path)

        if request:
            workspace_list = request.execute()
            for ws in workspace_list["workspace"]:
                if workspace_name == ws["name"]:
                    self.workspace = ws
                else:
                    pass
        else:
            print("workspace not exist")

        self.tag = Tag(workspaces)
        self.trigger = Trigger(workspaces)
        self.variable = Variable(workspaces)

    def _info(self):
        pprint(self.workspace)

    def _name(self):
        return self.workspace["name"]

    def _id(self):
        return self.workspace["workspaceId"]

    def _path(self):
        return self.workspace["path"]

    def _container_id(self):
        return self.workspace["containerId"]

    def _account_id(self):
        return self.workspace["accountId"]

    def create_tag(self, workspace_path, tag_info):
        print(tag_info["tag_name"])

        if tag_info["tag_type"] == "html":
            self.tag.create_html_tag(workspace_path, tag_info)

        if tag_info["tag_type"] == "ua_pv":
            self.tag.create_ga_pageview(workspace_path, tag_info)

        if tag_info["tag_type"] == "ua_event":
            self.tag.create_ga_event(workspace_path, tag_info)

        if tag_info["tag_type"] == "awct" or tag_info["tag_type"] == "sp":
            self.tag.create_gads(workspace_path, tag_info)

        if tag_info["tag_type"] == "flc":
            self.tag.create_flc(workspace_path, tag_info)

        if tag_info["tag_type"] == "fls":
            self.tag.create_fls(workspace_path, tag_info)

    def get_tag_by_name(self, workspace_path, tag_name):
        return self.tag.get_tag_by_name(workspace_path, tag_name)

    def tag_info(self, tag):
        self.tag.tag_info(tag)

    def connect_tag_trigger(self, tag, trigger):
        self.tag.connect_tag_trigger(tag, trigger)

    def create_trigger(self, workspace_path, trigger_info):
        self.trigger.create_trigger(workspace_path, trigger_info)

    def get_trigger_by_name(self, workspace_path, trigger_name):
        return self.trigger.get_trigger_by_name(workspace_path, trigger_name)

    def trigger_info(self, trigger):
        self.trigger.trigger_info(trigger)

    def create_variable(self, workspace_path, variable_info):
        self.variable.create_variable(workspace_path, variable_info)

    def get_variable_by_name(self, workspace_path, variable_name):
        return self.variable.get_variable_by_name(workspace_path, variable_name)

    def variable_info(self, variable):
        self.variable.variable_info(variable)

    # def create_workspace(self, container_path, workspaces, workspace_name, workspace_count):

    #     if not (workspace_name == self.workspace["name"]) and workspace_count < 3:
    #         return workspaces.create(
    #             parent=container_path, body={"name": workspace_name}
    #         ).execute()
    #     else:
    #         return "workspace is still exist"
