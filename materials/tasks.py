import os

from celery import shared_task
from django.core.mail import send_mail
from datetime import timedelta
from django.utils import timezone


from users.models import Subs
from users.models import User


@shared_task
def mail_update_treatise_info(treatise_id):
    subs_treatise = Subs.objects.filter(treatise=treatise_id)
    print(f"Найдено {len(subs_treatise)} подписок на курс {treatise_id}")
    for subs in subs_treatise:
        print(f"Отправка электронного письма на {subs.user.email}")
        send_mail(
            subject="Обновление подписки  курса",
            message=f'Курс {subs.course.title} был обновлен.',
            from_email=os.getenv('EMAIL_HOST_USER'),
            recipient_list=[subs.user.email],
            fail_silently=False
        )



@shared_task
def check_last_login():
    users = User.objects.filter(last_login__isnull=False)
    today = timezone.now()
    for user in users:
        if today - user.last_login > timedelta(days=30):
            user.is_active = False
            user.save()
            print(f'Пользователь {user.email} отключен')
        else:
            print(f'Пользователь {user.email} активен')