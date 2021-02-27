from pprint import pprint
from gtm_base import GTMBase


class GTMCreator(GTMBase):
    def __init__(self, service):
        super().__init__(service)

    def create_workspace(self, workspace, container_path, workspace_name, workspace_count):
        self.workspaces.create_workspace(
            workspace, container_path, workspace_name, workspace_count)

    def create_tag(self, workspace_path, tag_info):
        self.workspaces.create_tag(workspace_path, tag_info)

    def create_trigger(self, workspace_path, trigger_info):
        self.workspaces.create_trigger(workspace_path, trigger_info)

    def create_variable(self, workspace_path, variable_info):
        self.workspaces.create_variable(workspace_path, variable_info)

    def connect_tag_trigger(self, tag, trigger):
        self.workspaces.connect_tag_trigger(tag, trigger)