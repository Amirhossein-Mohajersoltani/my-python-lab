from random import choice
import pandas
import datetime as dt
import smtplib
import os
import dotenv

dotenv.load_dotenv()

MY_EMAIL = os.getenv("EMAIL")
MY_PASSWORD = os.getenv("PASSWORD")





# datetime
now = dt.datetime.now()
current_year = now.year
current_month = now.month
current_day = now.day



# users data
data_file = pandas.read_csv("./birthdays.csv")
data_file_dict = data_file.to_dict(orient="records")

for data_person in data_file_dict:
    name = data_person['name']
    email = data_person['email']
    year = data_person['year']
    month = data_person['month']
    day = data_person['day']
    if current_month == month and current_day == day:

        letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
        chosen_letter = choice(letters)
        replace_text = "[NAME]"
        with open(f"./letter_templates/{chosen_letter}") as letter_file:
            content = letter_file.read()
            content = content.replace(replace_text,name)

        with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL,password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,to_addrs=email,msg=f"Subject:Birthday Wisher\n\n{content}")


