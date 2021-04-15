from oauth2client.service_account import ServiceAccountCredentials
import gspread
from scripts.input_text import *
import csv


def read():
    f = open('source/data.csv', 'r', encoding='utf-8')
    rdr = csv.reader(f)
    array = []
    for line in rdr:
        array.append(line[0])
    f.close()
    return array


def spreadsheet_read():
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        'source/orpg-macro-admin.json', scope)
    gc = gspread.authorize(credentials)

    gc1 = gc.open(SHEETNAME).worksheet('시트1')
    gc2 = gc1.get_all_values()
    print(gc2)
    return gc2


def typing(text):
    input_text(text)


# setup()
# read()
