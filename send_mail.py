import smtplib


class Email:
    def __init__(self):
        self.my_email = "freebotpubg@gmail.com"
        self.password = '[YOUR_PASSWORD]'
        self.receiver_email = "alisadaintanvir@gmail.com"

    def send_email(self, new_content):
        try:
            with smtplib.SMTP('smtp.gmail.com') as connection:
                connection.starttls()
                connection.login(self.my_email, self.password)
                connection.sendmail(self.my_email, self.receiver_email, f"Subject:Birthday Wish \n\n {new_content}")
        except smtplib.SMTPException as error:
            print(f"an error occur while sending the mail:{error}")
        else:
            print("Email has been sent successfully.")
