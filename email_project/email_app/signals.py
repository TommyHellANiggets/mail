from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Subscriber

@receiver(post_save, sender=Subscriber)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:  # Проверяем, что запись создана
        subject = 'Новый клиент!'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['tommyhellaniggets@gmail.com']  # Определённый email, на который будет отправляться письмо

        # Текстовое содержание письма
        text_content = f'Новый клиент! Свяжитесь с ним по следующим данным: \nФИО: {instance.full_name}\nКомпания: {instance.company_name}\nТелефон: {instance.phone_number}\nEmail: {instance.email}'

        # HTML-содержание письма
        html_content = render_to_string('welcome_email.html', {'subscriber': instance})

        # Создаем объект EmailMultiAlternatives
        email = EmailMultiAlternatives(
            subject,
            text_content,
            email_from,
            recipient_list
        )

        # Добавляем HTML-содержание
        email.attach_alternative(html_content, "text/html")

        # Отправляем письмо
        email.send()
