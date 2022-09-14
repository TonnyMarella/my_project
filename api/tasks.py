from django.core.mail import send_mail
from MAIN_APP.celery import app
from MAIN_APP import settings


@app.task
def send_mail_task(user_email):
    send_mail('Your New Task', 'Write program Hello World', settings.EMAIL_HOST_USER, [user_email])
