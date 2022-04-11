import email
from email.parser import Parser
from pathlib import Path
import pandas as pd
import numpy as np
import os
import glob 


email_test = Path(r'sample\lay-k\_sent\1_')

data = {'id_mail': [],
        'x_origin': [],
        'from': [],
        'to': [],
        'subject': [],
        'date': [],
        'body': [],
        }

# sample\lay-k\_sent
# from pathlib import Path
# for path in Path('sample').rglob('*/all_documents/*'):
#     print(path.name)



# for f in glob.glob("/sample/*/all_documents/", recursive=True):
#     print(f)


for path in Path('sample').rglob('*\all_documents\*'):
# for path in Path(os.path.join(os.path.abspath(''),"sample")).rglob('*\all_documents\*'):
    with open(path, 'r') as file:
        # print(file.read())
        raw_email = Parser().parse(file)
        data["id_mail"].append(raw_email.get('Message-ID'))
        data["x_origin"].append(raw_email.get('X-Origin'))
        data["from"].append(raw_email.get('From'))
        data["to"].append(raw_email.get('To'))
        data["subject"].append(raw_email.get('Subject'))
        data["date"].append(raw_email.get('Date'))
        data["body"].append(raw_email.get_payload())





# with open(email_test,'r') as file:
#     raw_email = Parser().parse(file)
#     data["id_mail"].append(raw_email.get('Message-ID'))
#     data["x_origin"].append(raw_email.get('X-Origin'))
#     data["from"].append(raw_email.get('From'))
#     data["to"].append(raw_email.get('To'))
#     data["subject"].append(raw_email.get('Subject'))
#     data["date"].append(raw_email.get('Date'))
#     data["body"].append(raw_email.get_payload())
#     # append to data{}

df = pd.DataFrame(data)


print(df.head())
