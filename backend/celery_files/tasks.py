from celery import shared_task

from datetime import datetime, date

from database.models import User

@shared_task(ignore_result=False)
def send_daily_reminders():
    print('hello at main level remidner')
    today = datetime.now().date()
    users = User.query.filter(User.role=='user').all()
    for user in users:
        print(user.email)
        if user.last_login.date() != today:
            print('sending mail')
    return True

@shared_task(ignore_result=False)
def send_monthly_report():
    users = User.query.filter(User.role=='user').all()
    for user in users:
        print(user.email)
    return True
