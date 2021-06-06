import os
from intro import Setup
from subprocess import call
from environ_setter import Coldstart
from typing import *

class SendMail(): 
    cold = Coldstart()
    message = ''
    def __init__(self) -> None: 
        self.editor = os.getenv('EDITOR')
        initial_message = ""
        print(os.getenv('mailcache'))

        with open('./mailcache/mailcache.txt', 'w') as f: 
            f.write(initial_message)
            f.flush()
            call([self.editor, f.name])

        with open('./mailcache/mailcache.txt', 'r') as f: 
            message = f.read()

        print(message)

# Look at inheritance thing in Python
sms = SendMail()



