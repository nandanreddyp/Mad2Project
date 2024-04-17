import smtplib
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart, MIMEBase
from email.mime.application import MIMEApplication

def send_email(address, subject, message, attachment=None, filename=None, subtype=None):
    SMTP_SERVER_HOST = "smtp-relay.brevo.com"
    SMTP_SERVER_PORT = 587
    SENDER_EMAIL = "mayamahadevi96@gmail.com"
    SENDER_PASSWORD = "v5EqgW4LAYhdJ79V"

    msg = MIMEMultipart('alternative')
    msg["From"] = SENDER_EMAIL
    msg["To"] = address
    msg["Subject"] = subject
    msg.attach(MIMEText(message, "html"))

    if attachment:
        part = MIMEApplication(attachment.read(), _subtype=subtype)
        part.add_header("Content-Disposition", "attachment", filename= filename)
        msg.attach(part)
    
    s = smtplib.SMTP(host=SMTP_SERVER_HOST, port=SMTP_SERVER_PORT)
    s.login(SENDER_EMAIL, SENDER_PASSWORD)
    s.send_message(msg)
    s.quit()

# from database import *
from flask import render_template

def welcome_mail(email,name):
    template = render_template('welcome.html',name=name)
    send_email(email,'Welcome to E-Libri',template)
    return 200

def book_issued_mail(email,name,book_name):
    template = render_template('book_issued.html', name = name, book_name = book_name)
    send_email(email,'Your Request for a Book has been Accepted',template)
    return 200

def remind_visit_mail(email, name):
    template = render_template('reminder.html',name=name)
    send_email(email,'Make Reading a Daily Habit with E-Libri',template)
    return 200

def monthly_report_mail(email,name):
    template = render_template('monthly_report.html',name=name)
    send_email(email,'Personalized monthly report from E-Libri',template)

# from run import app
# with app.app_context():
#     email = 'jivrajsinghs123@gmail.com'
#     welcome_mail(email,'NandanReddy')
#     book_issued_mail(email,'NandanReddy','100 ways to die')
#     remind_visit_mail(email,'NandanReddy')
#     monthly_report_mail(email,'NandanReddy')