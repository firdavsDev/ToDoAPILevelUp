from celery import shared_task

from .email_verifycation import send_verification_email


@shared_task(
    name="send_verification_to_mail",
    autoretry_for=(Exception,),
    max_retries=3,
    retry_backoff=True,
)  # it will increase the time between retries)
def send_verification_to_mail(user_id, email):
    if send_verification_email(user_id, email):
        return "Sucsesfully"
    return "Failed"
