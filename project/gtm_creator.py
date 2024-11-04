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

    def create_trigger(self, workspace_path, trigger_info, filters):
        self.workspaces.create_trigger(workspace_path, trigger_info, filters)

    def create_variable(self, workspace_path, variable_info):
        self.workspaces.create_variable(workspace_path, variable_info)

    def create_builtin_variable(self, workspace_path):
        self.workspaces.create_builtin_variable(workspace_path)

    def connect_tag_trigger(self, tag, trigger):
        self.workspaces.connect_tag_trigger(tag, trigger)

    def create_version(self, workspace_path, container_version, version_name, notes):
        return self.workspaces.create_version(workspace_path, container_version, version_name, notes)