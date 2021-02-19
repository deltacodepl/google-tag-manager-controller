from pprint import pprint

class GTMTrigger():

    def __init__(self, workspaces): 
        
        if workspaces:
            self.triggers = workspaces.triggers()
        else:
            print("workspaces not exist")

    def _create_trigger(self, workspace_path, trigger_info):

        trigger = {
            'name': trigger_info['trigger_name'],
            'type': trigger_info['trigger_type']
        }

        try:
            return self.triggers.create(parent=workspace_path, body=trigger).execute()
        except:
            print("this trigger exists")

    def _get_trigger_by_name(self, workspace_path, trigger_name):
        triggers = self.triggers.list(parent=workspace_path).execute()
        result = None
        
        for trigger in triggers['trigger']:
            if(trigger['name'] == trigger_name):
                result = trigger
            else:
                pass    
        return result

    def _info(self, trigger):
        pprint(trigger)