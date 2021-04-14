from pprint import pprint


class Variable:
    def __init__(self, workspaces):

        if workspaces:
            self.variables = workspaces.variables()
            self.built_in_variable = workspaces.built_in_variables()

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
            print("💣 TRIGGER not Created 💣")

    def get_variables(self, workspace_path):
        variables = self.variables.list(parent=workspace_path).execute()
        return variables

    def get_built_in_variables(self, workspace_path):
        built_in_variables = self.built_in_variable.list(parent=workspace_path).execute()
        return built_in_variables

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

    def built_in_variable_info(self, built_in_variable):
        pprint(built_in_variable)