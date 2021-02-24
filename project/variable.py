from pprint import pprint


class Variable:
    def __init__(self, workspaces):

        if workspaces:
            self.variables = workspaces.variables()
        else:
            print("workspaces not exist")

    def create_variable(self, workspace_path, variable_info):

        variable = {
            "name": variable_info["variable_name"],
            "type": variable_info["variable_type"],
            "parameter": [
                {"key": "name", "type": "template", "value": variable_info["dlv_name"]}
            ],
        }
        try:
            return self.variables.create(parent=workspace_path, body=variable).execute()
        except:
            print("this variable exists")

    def get_variable_by_name(self, workspace_path, variable_name):
        variables = self.variables.list(parent=workspace_path).execute()
        result = None

        for variable in variables["variable"]:
            if variable["name"] == variable_name:
                result = variable
            else:
                pass
        return result

    def variable_info(self, variable):
        pprint(variable)
