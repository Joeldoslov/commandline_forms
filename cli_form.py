from os import system
import msvcrt
# import re


class cli_form:

    def __init__(self):
        self.form_text = ""
        system("cls")

    # def _filter_(self, ch: str, text: str):
    #     regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    #     if(regex.search(ch) == None) and not ch.isalnum():
    #         if str(ch) == 'KEY_BACKSPACE' or ch == '\x08':
    #             return text[:-1]
    #         else:
    #             return text
    #     else:
    #         return ''

    def inputpwd(self, input_string: str = "Password"):
        _ret_string = ""
        ch = ''
        while True:
            _ret_string += str(ch)
            system("cls")
            print(self.form_text)
            print(input_string + "*" * len(_ret_string))
            ch = str(msvcrt.getch())
            ch = ch.strip("b'").strip("'")
            # if ch == '\b':
            #     _ret_string = _ret_string[:-1]
            if ch == '\\r' or ch == '\\n':
                break
        self.form_text += input_string + ("*" * len(_ret_string)) + "\n"
        return _ret_string

    def input(self, input_string: str = ""):
        _input = input(input_string)
        self.form_text += input_string + _input + "\n"
        return _input

    def print(self, print_string: str = ""):
        self.form_text += print_string + "\n"
        print(print_string)

    def choice(self, input_string: str = "Yes/No"):
        _inputchoice = input(input_string)
        self.form_text += input_string + _inputchoice + "\n"
        if 'y' in _inputchoice or 'Y' in _inputchoice:
            return 'y'
        if 'n' in _inputchoice or 'N' in _inputchoice:
            return 'n'
