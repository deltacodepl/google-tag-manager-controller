from pprint import pprint

class GTMWorkspace():

    def __init__(self, workspaces, container_path, workspace_name):
        self.workspaces = workspaces
        request = workspaces.list(parent=container_path)
        
        if request:
            workspaces = request.execute()
            for ws in workspaces['workspace']:
                if (workspace_name == ws['name']):        
                    self.workspace = ws
                else:
                    pass
        else:
            print("workspace not exist")

    def _create(self, container_path, workspace_name, workspace_count):

        if not (workspace_name == self.workspace['name']) and workspace_count < 3:
            return self.workspaces.create(parent=container_path, body={'name': workspace_name}).execute()
        else:
            print('workspace is still exist')



    def _info(self):
        pprint(self.workspace)

    def _name(self):
        return self.workspace['name']

    def _id(self):
        return self.workspace['workspaceId']

    def _path(self):
        return self.workspace['path']

    def _container_id(self):
        return self.workspace['containerId']

    def _account_id(self):
        return self.workspace['accountId']