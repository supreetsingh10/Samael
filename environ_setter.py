import os 
from typing import * 


class Coldstart: 
    def __init__(self) -> None: 
        os.environ['shadow'] = '/home/supreetsingh/Documents/SavedPrograms/Python/samael/samael/src/security/shadow.json'
        os.environ['mailcache'] = '/home/supreetsingh/Documents/SavedPrograms/Python/samael/samael/src/mailcache/mailcache.txt'
        os.environ['drafts'] = '/home/supreetsingh/Documents/SavedPrograms/Python/samael/samael/src/drafts/'


