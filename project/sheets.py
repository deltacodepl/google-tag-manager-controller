import json
from googleapiclient.discovery import build
from google.oauth2 import service_account

def setup(sheets_id):
    scopes = ['https://www.googleapis.com/auth/spreadsheets']
    service_account_file = 'conf/service_account.json'
    creds = None
    creds = service_account.Credentials.from_service_account_file(
            service_account_file, scopes=scopes)

    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    return sheet

def read_sheets(sheets_id, sheet, tab):
    result = sheet.values().get(spreadsheetId = sheets_id, range = tab).execute()
    values_as_list = result.get('values', [])
    print(values_as_list)

def get_listed_values(sheets_id, sheet, tab):
    result = sheet.values().get(spreadsheetId = sheets_id, range = tab).execute()
    values_as_list = result.get('values', [])
    return values_as_list

def get_json_values(sheets_id, sheet, tab):
    pass
    # TODO #
    # result = sheet.values().get(spreadsheetId = sheets_id, range = tab).execute()
    # values_as_list = result.get('values', [])
    # for val in values_as_list:
    #     pass
    # print(val_as_json)

def upload_df_sheets(sheets_id, df, sheet, tab):
    
    body=dict(
        majorDimension='ROWS',
        values=df.T.reset_index().T.values.tolist()
    )

    request = sheet.values().update(
        spreadsheetId=sheets_id, 
        range=tab, 
        valueInputOption='USER_ENTERED', 
        body=body
    )

    request.execute()