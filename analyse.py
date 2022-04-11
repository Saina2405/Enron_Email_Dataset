import email
from email.parser import Parser
from pathlib import Path


email_test = Path(r'sample\lay-k\_sent\1_')

with open(email_test,'r') as file:
    raw_email = Parser().parse(file)
print(raw_email.get_payload())