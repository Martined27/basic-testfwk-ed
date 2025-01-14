import logging
import os
import re
import requests

SESSION = requests.Session()
APP_URL = os.getenv("APP_URL", "http://localhost:8080")
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "")

LOG = logging.getLogger()

class HideSensitiveData(logging.Filter):
    def filter(self, record):
       record.msg = str(record.msg).replace(ADMIN_PASSWORD, "*******")
       record.msg = re.sub(r"Authorization: Bearer [a-zA-Z0-9]+", "Authorization: Bearer *******", record.msg)
       return True
    
LOG.addFilter(HideSensitiveData())
     