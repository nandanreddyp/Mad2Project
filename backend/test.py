# # reset app
# import os
# db_path = os.path.join(os.getcwd(),'database','database.db')
# if os.path.exists(db_path): os.remove(db_path)





# from celery_files.tasks import send_daily_reminders
# from run import app

# with app.app_context():

#     send_daily_reminders()
