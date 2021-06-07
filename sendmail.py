import os
from intro import Setup
from subprocess import call
from environ_setter import Coldstart
from typing import *
from shutil import copy

class SendMail(): 
    cold = Coldstart()
    message = ''

    def cleanUp(self, flag) -> None: 
        with open(os.getenv('mailcache'), 'a') as f: 
            if flag == True: 
                print('Enter the name of the save file')
                self.SaveFileName = input('Name : ')
                copy(os.getenv('mailcache'), os.getenv('drafts') + self.SaveFileName)

            f.truncate(0)


    def questionSave(self) -> bool:
        while True: 
            try: 
                print('Do you want to save the file in sent messages? Enter yes or no')
                self.ans = input('Answer: ').lower().strip()
                if self.ans[0] not in ['y', 'n']: 
                    raise ValueError
                else: 
                    self.ans = self.ans[0]
                    break
            except ValueError: 
                print('Enter a valid answer')

        return True if self.ans == 'y' else False


    def __init__(self) -> None: 
        self.editor = os.getenv('EDITOR')
        initial_message = ''

        with open(os.getenv('mailcache') , 'w+') as f: 
            f.write(initial_message)
            f.flush()
            call([self.editor, f.name])


        with open(os.getenv('mailcache'), 'r') as f: 
            message = f.read()

        print(message)
        self.cleanUp(self.questionSave())

# Look at inheritance thing in Python
sms = SendMail()



