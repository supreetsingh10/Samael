import os 
from typing import * 


class Coldstart: 
    def __init__(self) -> None: 
        os.environ['shadow'] = '~/Documents/SavedPrograms/Python/samael/samael/src/security/shadow.json'
        os.environ['mailcache'] = '~/Documents/SavedPrograms/Python/samael/samael/src/mailcache/'
        os.environ['drafts'] = '~/Documents/SavedPrograms/Python/samael/samael/src/drafts/'


