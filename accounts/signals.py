from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts.tasks import send_verification_to_mail
from .email_verifycation import send_verification_email

from .models import CustomUser


@receiver(post_save, sender=CustomUser)
def send_email_code(sender, instance, created, **kwargs):
    if created:
        # send_verification_email(instance.id, instance.email)
        send_verification_to_mail.delay(instance.id, instance.email)
