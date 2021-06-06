import email.utils
import smtplib as sam
import os
from typing import *
from getpass import getpass
from secure import Encrypt
from environ_setter import Coldstart

# Add possible accounts 
# Make a file for storing the username and passoword in the system and make it encrypted. 

class Setup: 
    def __init__(self) -> None: 
        cold = Coldstart()
        #self.Mailer()
        print('Continue old session? (y/n)')

        while True: 
            try: 
                old_session = str(input('Answer : '))
                if old_session.lower().strip()[0] in ['y', 'n']: 
                    break
                raise ValueError
            except ValueError: 
                print('Enter a valid choice')

        old_session = old_session.lower().strip()[0]
        if old_session == 'y': 
            print('Old session code here')
        else: 
            self.Mailer()


    def SetAccount(self) -> list[str, int] : 
        print(''' Possible accounts are:\n 1.gmail.com\n 2.Yahoo.com\n 3.Outlook.com\n 
Select a number ''')
        self.Emailclients = {
                    1 : ['smtp.gmail.com', 587], 
                    2 : ['smtp.mail.yahoo.com', 465],
                    3 : ['smtp-mail.outlook.com', 587]
                }

        while True: 
            try: 
                choice = int(input('Enter your choice '))
                if choice > 3 or choice < 1: 
                    raise ValueError('Choice should be between 1 and 3')
                break
            except ValueError: 
                print('Try again')

        return self.Emailclients[choice]

    def Mailer(self) -> None: 
        self.host, self.port = self.SetAccount(); 
        self.smtpObj = sam.SMTP(self.host, self.port)
        self.smtpObj.starttls()
        enc = Encrypt()

        # This input will later be used to get the stored users.  
        self.NewUser = self.getUsername()  
        try:
            # If there is no shadow file then it will raise an exception
            # It will also raise an exception if the user is new. 

            response = enc.checkUser(self.NewUser)
            self.NewUser, self.secret = response['username'], enc.decodePass(response['password'])
            #self.smtpObj.login(username, password) <- This is test code. 
        except: 
            # This will add a new user. 
            # TODO: The code is currently overwriting the shadow file
            self.secret = getpass()
            enc.encryptUserPass(self.NewUser, self.secret, self.host)

        self.loggeduser = self.smtpObj.login(self.NewUser, self.secret)

        self.smtpObj.quit()

    def getUsername(self) -> str: 
        return input('Enter your username: ')





