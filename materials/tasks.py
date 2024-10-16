from celery import shared_task
from django.core.mail import send_mail
from materials.models import Course

@shared_task
def send_course_update_email(user_email, course_name):
    subject = f'Обновление курса: {course_name}'
    message = f'Курс "{course_name}" был обновлен. Проверьте обновления!'
    send_mail(subject, message, 'from@example.com', [user_email])