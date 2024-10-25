from pprint import pprint
from tag import Tag
from trigger import Trigger
from variable import Variable


class Workspace:
    def __init__(self, service):
        self.workspaces = service.accounts().containers().workspaces()

    def get_workspaces(self, account_id, container_id):
        path = f"accounts/{account_id}/containers/{container_id}"
        return self.workspaces.list(parent=path).execute()

    def set_workspace(self, workspace_list, workspace_name):

        for ws in workspace_list["workspace"]:
            if ws["name"] == workspace_name:
                self.workspace = ws
            else:
                pass

        self.tag = Tag(self.workspaces)
        self.trigger = Trigger(self.workspaces)
        self.variable = Variable(self.workspaces)

    def print_info(self):
        pprint(self.workspace)

    def print_workspace_val(self):
        vals = self.workspace

    def get_name(self):
        return self.workspace["name"]

    def get_id(self):
        return self.workspace["workspaceId"]

    def get_path(self):
        return self.workspace["path"]

    def create_workspace(self, workspace, container_path, workspace_name, workspace_count):

        if workspace_count < 3:
            try:
                self.workspaces.create(
                    parent=container_path, body={"name": workspace_name}
                ).execute()
            except:
                print("This Workspace exsists!")
        else:
            print("workspace limit! you cannot creat more than 3")

    def create_version(self, workspace_path, container_version, version_name, notes):
        
        request = self.workspaces.create_version(
            path=workspace_path, body={"name": version_name, "notes": notes}
        )

        response = request.execute()

        get_cv = response.get("containerVersion")

        return get_cv

        #TODO: RETURN CONTAINER VERSION #

        # version = gtm_manager.version.GTMVersion(
        #     version=response.get("containerVersion"), service=self.service
        # )

        # if version.containerVersionId == "0":
        #     raise Exception(
        #         "Could not create version from workspace. Please visit {} for details".format(
        #             self.tagManagerUrl
        #         )
        #     )

        # return version

    
    def create_tag(self, workspace_path, tag_info):

        if tag_info["tag_type"] == "html":
            self.tag.create_html_tag(workspace_path, tag_info)

        if tag_info["tag_type"] == "ua_pv":
            self.tag.create_ga_pageview(workspace_path, tag_info)

        if tag_info["tag_type"] == "gaawe":
            self.tag.create_ga4_tag(workspace_path, tag_info)
            #self.tag.create_ga_event(workspace_path, tag_info)

        if tag_info["tag_type"] == "awct" or tag_info["tag_type"] == "sp":
            self.tag.create_gads(workspace_path, tag_info)

        if tag_info["tag_type"] == "flc":
            self.tag.create_flc(workspace_path, tag_info)

        if tag_info["tag_type"] == "fls":
            self.tag.create_fls(workspace_path, tag_info)


    def create_trigger(self, workspace_path, trigger_info, filters):
        self.trigger.create_trigger(workspace_path, trigger_info, filters)

    def create_variable(self, workspace_path, variable_info):
        self.variable.create_variable(workspace_path, variable_info)

    def connect_tag_trigger(self, tag, trigger):
        self.tag.connect_tag_trigger(tag, trigger)

    def get_tags(self, workspace_path):
        return self.tag.get_tags(workspace_path)

    def get_tag_by_name(self, workspace_path, tag_name):
        return self.tag.get_tag_by_name(workspace_path, tag_name)

    def get_triggers(self, workspace_path):
        return self.trigger.get_triggers(workspace_path)

    def get_trigger_by_name(self, workspace_path, trigger_name):
        return self.trigger.get_trigger_by_name(workspace_path, trigger_name)

    def get_variables(self, workspace_path):
        return self.variable.get_variables(workspace_path)

    def get_built_in_variables(self, workspace_path):
        return self.variable.get_built_in_variables(workspace_path)

    def get_variable_by_name(self, workspace_path, variable_name):
        return self.variable.get_variable_by_name(workspace_path, variable_name)

    def print_tag_info(self, tag):
        self.tag.tag_info(tag)

    def print_trigger_info(self, trigger):
        self.trigger.trigger_info(trigger)

    def print_variable_info(self, variable):
        self.variable.variable_info(variable)

    def print_built_in_variable_info(self, built_in_variable):
        self.variable.built_in_variable_info(built_in_variable)