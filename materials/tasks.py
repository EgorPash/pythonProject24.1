from celery import shared_task
from django.core.mail import send_mail
from materials.models import Subscription

@shared_task
def send_course_update_email(course_id):
    subscriptions = Subscription.objects.filter(course_id=course_id)
    for subscription in subscriptions:
        send_mail(
            'Обновление курса',
            'Курс был обновлен. Проверьте новые материалы!',
            'from@example.com',
            [subscription.user.email],
            fail_silently=False,
        )