import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path  # same as os.path


html = Template(Path('index.html').read_text())
email = EmailMessage()
sender_name = input('What is your name? ')
receiver_mail = input('Which mail do you want to send your massage to? ')
mail_subject = input('What it the subject of the mail? ')
sender_mail = input('Which email do you want to use? ')
sender_password = input('your password please! ')
receiver_name = input('What is the name of the receiver? ')

email['from'] = sender_name
email['to'] = receiver_mail
email['subject'] = mail_subject

email.set_content(html.substitute({'name': receiver_name}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(sender_mail, sender_password)
    smtp.send_message(email)
    print('all good boss!')
