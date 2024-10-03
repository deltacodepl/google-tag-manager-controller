from google_auth_oauthlib.flow import Flow

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

parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter, parents=[tools.argparser]
    )
    flags = parser.parse_args([])

    flow = client.flow_from_clientsecrets(
        client_secrets_path,
        scope=scope,
        message=tools.message_if_missing(client_secrets_path),
    )

    storage = file.Storage(api_name + ".dat")
    credentials = storage.get()
    if credentials is None or credentials.invalid:
        credentials = tools.run_flow(flow, storage, flags)
    http = credentials.authorize(http=httplib2.Http())


print('Please go here to authorize the access.')
print(authorization_url)