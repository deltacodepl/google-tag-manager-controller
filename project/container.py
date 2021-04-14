from pprint import pprint


class Container:
    def __init__(self, service):
        self.containers = service.accounts().containers()

    def get_containers(self, account_id):
        account_path = f"accounts/{account_id}"
        return self.containers.list(parent=account_path).execute()

    def set_container(self, container_list, container_name):
        for con in container_list["container"]:
            if con["name"] == container_name:
                self.container = con
            else:
                pass

    def print_info(self):
        pprint(self.container)

    def get_name(self):
        return self.container["name"]

    def get_id(self):
        return self.container["containerId"]

    def get_path(self):
        return self.container["path"]

    def get_container_version(self):        
        versions = self.containers.versions
        return versions
