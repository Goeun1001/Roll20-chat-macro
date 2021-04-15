from scripts import read
from scripts import input_text
from time import sleep
import inquirer


def setup():
    input_text.setup()


def print_list():
    array = read.read()
    i = 0
    while i < len(array):
        questions = [
            inquirer.List('text',
                          message="다음 대사를 선택해주세",
                          choices=[array[i], '패스'],
                          ),
        ]
        answers = inquirer.prompt(questions)

        if answers['text'] != '패스':
            input_text.input_text(answers['text'])
            sleep(len(answers['text']) * 0.2)

        i += 1


setup()
print_list()


