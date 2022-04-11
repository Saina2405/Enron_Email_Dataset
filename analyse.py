from email.parser import Parser
from pathlib import Path
import pandas as pd
import numpy as np
import os

# creating empty dict for our df
data = {
    'id_mail': [],
    'x_origin': [],
    'from': [],
    'to': [],
    'subject': [],
    'date': [],
    'body': [],
}

# open each file and allocate the elements to the dict predefine
# sample_path = Path("""sample""")
# for path in sample_path.rglob(r'*\all_documents\*'):

for path in Path('ressources\maildir').rglob(r'*\all_documents\*'):
    with open(path, 'r') as file:
        raw_email = Parser().parse(file)
        data["id_mail"].append(raw_email.get('Message-ID'))
        data["x_origin"].append(raw_email.get('X-Origin'))
        data["from"].append(raw_email.get('From'))
        data["to"].append(raw_email.get('To'))
        data["subject"].append(raw_email.get('Subject'))
        data["date"].append(raw_email.get('Date'))
        data["body"].append(raw_email.get_payload())

# creating the df with our dict
df = pd.DataFrame(data)
print(df.shape)

# to csv
to_csv = input("Do you want to do a csv file ?").lower()
if to_csv == "y":
    df.to_csv("data/v2.csv")
else:
    pass
