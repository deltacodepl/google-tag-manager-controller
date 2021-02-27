from pprint import pprint


class Account:
    def __init__(self, service):
        self.accounts = service.accounts()

    def get_accounts(self):
        return self.accounts.list().execute()

    def set_account(self, account_id):
        request = self.accounts.get(path=f"accounts/{account_id}")
        if request:
            self.account = request.execute()
        else:
            print("account not exist")

    def print_info(self):
        pprint(self.account)

    def get_name(self):
        return self.account["name"]

    def get_id(self):
        return self.account["accountId"]

    def get_path(self):
        return self.account["path"]
