import pandas as pd
from datetime import datetime as dt
import random
from send_mail import Email

email = Email()
today = dt.now()
today_tuple = (today.month, today.day)

data = pd.read_csv('birthdays.csv')
df = pd.DataFrame(data)
birthday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in df.iterrows()}

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    with open(f"letter_templates/letter_{random.randint(0,3)}.txt", 'r') as letter_file:
        letter = letter_file.read()
        letter = letter.replace("[NAME]", birthday_person['name'])
        email.send_email(letter)
