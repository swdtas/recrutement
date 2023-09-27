from django.db import models

# Create your models here.
from django.core.mail import EmailMessage

def send_new_job_notification(user, job_listing):
    subject = 'Nouvelle offre d\'emploi disponible'
    message = f'Une nouvelle offre d\'emploi "{job_listing.title}" est disponible. Consultez-la sur notre site.'
    from_email = 'sawadogotassere30@gmail.com'
    recipient_list = [user.email]
    email = EmailMessage(subject, message, from_email, recipient_list)
    email.send()
