from pprint import pprint


class Account:
    def __init__(self, accounts, account_id):
        self.path = f"accounts/{account_id}"
        request = accounts.get(path=self.path)

        if request:
            self.account = request.execute()
        else:
            print("account not exist")

    def _info(self):
        pprint(self.account)

    def _name(self):
        return self.account["name"]

    def _id(self):
        return self.account["accountId"]

    def _path(self):
        return self.account["path"]
