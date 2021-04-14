from oauth2client.service_account import ServiceAccountCredentials
import gspread

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(
        'orpg-macro-admin.json', scope)
gc = gspread.authorize(credentials)

gc1 = gc.open("꼬리가 살랑거려요 예제").worksheet('시트1')
gc2 = gc1.get_all_values()
print(gc2)
