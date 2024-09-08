import smtplib
from email.message import EmailMessage

def send_email(date,quantity):
    email_address='waterconsumption2@gmail.com'
    email_password='147852wc'
    text_message="today {} was a {} consumption of water".format(date,quantity)
    recipients = ['giladroy1@gmail.com', 'nadavgil18@gmail.com']

    msg = EmailMessage()
    msg['Subject'] = 'there is new massage'
    msg['To'] = ", ".join(recipients)
    msg.set_content(text_message)

    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.login(email_address , email_password)

        smtp.send_message(msg)