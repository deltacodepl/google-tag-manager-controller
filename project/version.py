from pprint import pprint

class GTMVersion():

    def __init__(self, workspaces): 
        
        if workspaces:
            self.workspaces = workspaces
        else:
            print("workspaces not exist")

    def _version(self):
        pass