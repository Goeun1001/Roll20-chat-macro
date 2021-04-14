from oauth2client.service_account import ServiceAccountCredentials
import gspread
from scripts.input_text import *


def read():
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        '../orpg-macro-admin.json', scope)
    gc = gspread.authorize(credentials)

    gc1 = gc.open("꼬리가 살랑거려요 예제").worksheet('시트1')
    gc2 = gc1.get_all_values()
    # print(gc2)
    divide(gc2)


def divide(array):
    i = 0
    zero_arr = []
    one_arr = []
    while i < len(array):
        if array[i][0] == '0':
            zero_arr.append(array[i])
        elif array[i][0] == '1':
            one_arr.append(array[i])
        i += 1

    if one_arr is not None:
        typing(one_arr)


def typing(array):
    i = 0
    while i < len(array):
        text = ""
        if array[i][1] == "desc":
            text += "/desc "
            text += array[i][2]
        if array[i][1] == "emas":
            text += "/emas "
            text += '"' + array[i][2] + '"'
        if array[i][1] == "":
            text += array[i][2]

        print(text)
        input_text(text)
        i += 1


setup()
read()
