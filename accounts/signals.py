from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from accounts.tasks import send_verification_to_mail

from .models import CustomUser


@receiver(post_save, sender=CustomUser)
def send_email_code(sender, instance, created, **kwargs):
    if created:
        # send email verification
        task_id = send_verification_to_mail.delay(instance.email)