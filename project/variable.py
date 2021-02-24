from pprint import pprint


class Variable:
    def __init__(self, workspaces):

        if workspaces:
            self.variables = workspaces.variables()
        else:
            print("workspaces not exist")

    def create_variable(self, workspace_path, variable_info):

        variable = {
            "name": variable_info["name"],
            "type": variable_info["type"],
            "parameter": [
                {
                    "key": variable_info["param_key"],
                    "type": "template",
                    "value": variable_info["value"],
                }
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
