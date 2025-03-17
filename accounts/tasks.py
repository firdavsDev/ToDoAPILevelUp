from celery import shared_task

from accounts.email_verifycation import send_verification_email


@shared_task(
    name="send_verification_to_mail",
    # bind=True,  # bind the task to the task instance it means the first argument will be the task instance itself
    autoretry_for=(Exception,),
    max_retries=3,
    retry_backoff=True,  # it will increase the time between retries
)
def send_verification_to_mail(email):
    send_verification_email(email)

    return "Sucsesfully"
