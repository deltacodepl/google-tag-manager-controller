from pprint import pprint


class Trigger:
    def __init__(self, workspaces):

        if workspaces:
            self.triggers = workspaces.triggers()
        else:
            print("workspaces not exist")

    def create_trigger(self, workspace_path, trigger_info):

        trigger = {
            "name": trigger_info["trigger_name"],
            "type": trigger_info["trigger_type"],
        }

        try:
            return self.triggers.create(parent=workspace_path, body=trigger).execute()
        except:
            print("this trigger exists")

    def get_trigger_by_name(self, workspace_path, trigger_name):
        triggers = self.triggers.list(parent=workspace_path).execute()

        for trigger in triggers["trigger"]:
            if trigger["name"] == trigger_name:
                return trigger
            else:
                pass

    def trigger_info(self, trigger):
        pprint(trigger)
