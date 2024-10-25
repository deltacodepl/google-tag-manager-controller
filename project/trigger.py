from pprint import pprint


class Trigger:
    def __init__(self, workspaces):

        if workspaces:
            self.triggers = workspaces.triggers()
        else:
            print("workspaces not exist")

    def create_trigger(self, workspace_path, trigger_info, filters):

        trigger_head = {
            "name": trigger_info["trigger_name"],
            "type": trigger_info["trigger_type"],
        }
        if filters:
            trigger = {**trigger_head, **filters}
            repr(trigger)
        else:
            trigger = trigger_head
        try:
            self.triggers.create(parent=workspace_path, body=trigger).execute()
            print(" 🎉 TRIGGER Created 🎉")
            return self.triggers
        except Exception as e:
            print(f"💣 TRIGGER not Created 💣 {e}")

    def get_triggers(self, workspace_path):
        triggers = self.triggers.list(parent=workspace_path).execute()
        return triggers

    def get_trigger_by_name(self, workspace_path, trigger_name):
        triggers = self.triggers.list(parent=workspace_path).execute()
        if triggers:
            for trigger in triggers["trigger"]:
                if trigger["name"] == trigger_name:
                    return trigger
        return None

    def trigger_info(self, trigger):
        pprint(trigger)
