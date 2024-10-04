from sys import api_version


from httplib2.auth import auth_param
from oauth2client import client
from oauth2client import tools
from oauth2client import file

from oauth2client import GOOGLE_REVOKE_URI
import httplib2

api_name = "tagmanager"
api_version = "V2"
# flow = Flow.from_client_secrets_file(
#     'conf/client_secret.json',
#     scopes = [
#       'https://www.googleapis.com/auth/photoslibrary.readonly',
#     ],
# )
# flow.redirect_uri = 'https://localhost:8080/auth/google/callback'
# # flow.run_local_server()
# authorization_url, state = flow.authorization_url(
#     access_type='offline',
#     include_granted_scopes='true'
# )

# parser = argparse.ArgumentParser(
#         formatter_class=argparse.RawDescriptionHelpFormatter, parents=[tools.argparser]
#     )
# flags = parser.parse_args([])

scope = [
    'https://www.googleapis.com/auth/tagmanager.readonly'
]

flags = None
flow = client.flow_from_clientsecrets(
    'conf/client_secrets.json',
    scope=scope,
    # message=tools.message_if_missing(client_secrets_path),
)

storage = file.Storage(api_name + ".dat")
credentials = storage.get()
if credentials is None or credentials.invalid:
    credentials = tools.run_flow(flow, storage, flags)
http = credentials.authorize(http=httplib2.Http())

# credentials.revoke(http)
print('Please go here to authorize the access.')
print(http)
print(repr(credentials))