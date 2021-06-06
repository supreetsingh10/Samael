import os 
from typing import * 
import json, base64

class Encrypt: 
    def checkUser(self, user: str) -> dict[str, str]: 
        with open(r'./security/shadow.json', 'r') as f: 
            creds = json.load(f)
            return creds[user]

    def decodePass(self, password: str) -> str: 
        return base64.b64decode(password).decode()

    def encryptUserPass(self, user: str, password: str, host: str) -> None:
        self.username = user 
        self.password = base64.b64encode(password.encode())
        self.dumppass = self.password.decode('ascii')
        self.host = host
        with open(r'./security/shadow.json', 'w') as f: 
            self.data = {
                    self.username: 
                        {
                        'username': self.username,
                        'password': self.dumppass,
                        'host': self.host
                        }
                    }
            json.dump(self.data, f)
        return None
