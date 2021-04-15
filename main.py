from pick import pick
from scripts import read
from scripts import input_text
from time import sleep


def setup():
    input_text.setup()


def print_list():
    array = read.read()
    i = 0
    while i < len(array):
        title = '다음에 입력할 대사를 선택하세요: '
        options = [array[i], '패스']
        option, index = pick(options, title)
        if index == 0:
            input_text.input_text(option)
            sleep(len(option) * 0.2)

        i += 1


setup()
print_list()


