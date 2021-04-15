from scripts import read
from scripts import input_text
import inquirer


def setup():
    input_text.setup()


def print_list():
    array = read.read()
    i = 0
    while i < len(array):
        questions = [
            inquirer.List('text',
                          message="다음에 입력할 대사를 선택하세요",
                          choices=[array[i], '패스'],
                          ),
        ]
        answers = inquirer.prompt(questions)

        if answers['text'] != '패스':
            input_text.input_text(answers['text'])

        i += 1


setup()
print_list()


