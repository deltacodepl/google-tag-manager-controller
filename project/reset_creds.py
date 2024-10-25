"""
Shows basic usage of the Apps Script API.
Call the Apps Script API to create a new script project, upload a file to the
project, and log the script's URL to the user.
"""
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient import errors
from googleapiclient.discovery import build

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/script.projects"]

SCOPES = ["https://www.googleapis.com/auth/tagmanager.readonly"]

SAMPLE_CODE = """

function helloWorld() {
  console.log("Hello, world!");
}
""".strip()

SAMPLE_MANIFEST = """
{
  "timeZone": "Europe/Warsaw",
  "exceptionLogging": "CLOUD"
}
""".strip()


def main():
    """Calls the Apps Script API."""
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            print("Refreshing creds ....")
            creds.refresh(Request())
        else:
            print("Running the flow")
            flow = InstalledAppFlow.from_client_secrets_file(
                "conf/client_secrets.json", SCOPES
            )
            creds = flow.run_local_server(port=8080) # gareports OAuth redirect_uri port
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        service = build("script", "v1", credentials=creds)
        print(creds.to_json())
        # Call the Apps Script API
        # Create a new project
        request = {"title": "My Script"}
        response = service.projects().create(body=request).execute()

        # Upload two files to the project
        request = {
            "files": [
                {"name": "hello", "type": "SERVER_JS", "source": SAMPLE_CODE},
                {
                    "name": "appsscript",
                    "type": "JSON",
                    "source": SAMPLE_MANIFEST,
                },
            ]
        }
        response = (
            service.projects()
            .updateContent(body=request, scriptId=response["scriptId"])
            .execute()
        )
        print("https://script.google.com/d/" + response["scriptId"] + "/edit")
    except errors.HttpError as error:
        # The API encountered a problem.
        print(error.content)


if __name__ == "__main__":
    main()
