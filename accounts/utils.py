from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils import timezone

def send_password_reset_email(user, reset_link):
    subject = "Reset Your SIQNet Password"
    from_email = 'SIQNet <noreply@siqnet.com>'
    to_email = user.email

    text_content = "Click the link to reset your password."
    html_content = render_to_string('password_reset.html', {
        'user': user,
        'reset_link': reset_link,
        'current_year': timezone.now().year,
    })

    email = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
    email.attach_alternative(html_content, "text/html")
    email.send()

def send_welcome_email(user, verification_link):
    subject = "Welcome to SIQNet 🎉"
    from_email = 'SIQNet <noreply@siqnet.com>'
    to_email = user.email

    text_content = "Welcome to SIQNet! Click the link to verify your email."
    html_content = render_to_string('emails/welcome.html', {
        'user': user,
        'verification_link': verification_link,
        'current_year': timezone.now().year,
    })

    email = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
    email.attach_alternative(html_content, "text/html")
    email.send()
