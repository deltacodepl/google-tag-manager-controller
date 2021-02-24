from pprint import pprint
from account import Account


class Container(Account):
    def __init__(self, account_path, containers, container_name):
        request = containers.list(parent=account_path)

        if request:
            containers = request.execute()
            for con in containers["container"]:
                if con["name"] == container_name:
                    self.container = con
                else:
                    print("this container not exist")
        else:
            print("container not exist")

    def _info(self):
        pprint(self.container)

    def _name(self):
        return self.container["name"]

    def _id(self):
        return self.container["containerId"]

    def _path(self):
        return self.container["path"]
