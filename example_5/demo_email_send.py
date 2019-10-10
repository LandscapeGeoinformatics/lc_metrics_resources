# using SendGrid's Python Library - https://github.com/sendgrid/sendgrid-python
import sendgrid
import os
from sendgrid.helpers.mail import Mail



message = sendgrid.helpers.mail.Mail(
    from_email='alexander.kmoch@ut.ee',
    to_emails='allixender@gmail.com',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='and easy to do anywhere, even with Python')

sg = sendgrid.SendGridAPIClient("xxx")
response = sg.send(message)
print(response.status_code)
print(response.body)
print(response.headers)
