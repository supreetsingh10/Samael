import email.utils
import smtplib as sam
import os
from typing import *
from getpass import getpass
from secure import Encrypt

# Add possible accounts 
# Make a file for storing the username and passoword in the system and make it encrypted. 

class Setup: 
    def __init__(self) -> None:
        self.host = 'smtp.gmail.com'
        self.port = 587
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
            enc.encryptUserPass(self.NewUser, self.secret)

        self.loggeduser = self.smtpObj.login(self.NewUser, self.secret)
        print(self.loggeduser)

        self.smtpObj.quit()

    def getUsername(self) -> str: 
        return input('Enter your username: ')


enc = Setup()


