from celery import shared_task

from datetime import datetime, date

from database.models import User

from send_mail import remind_visit_mail, monthly_report_mail

@shared_task(ignore_result=False)
def send_daily_reminders():
    today = datetime.now().date()
    users = User.query.filter(User.role=='user').all()
    for user in users:
        if user.last_login.date() != today:
            remind_visit_mail(user.email, user.f_name+' '+user.l_name)
    print('sent reminders')
    return True

@shared_task(ignore_result=False)
def send_monthly_report():
    users = User.query.filter(User.role=='user').all()
    for user in users:
        monthly_report_mail(user.email, user.f_name+' '+user.l_name)
    print('sent montly report')
    return True
