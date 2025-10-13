from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils import timezone

def send_mention_alert_email(user, mentioner_username, post_link):
    subject = f"{mentioner_username} mentioned you in a post!"
    from_email = 'SIQNet <noreply@siqnet.com>'
    to_email = user.email

    text_content = f"{mentioner_username} mentioned you on SIQNet. Click to view."
    html_content = render_to_string('emails/mention_alert.html', {
        'user': user,
        'mentioner_username': mentioner_username,
        'post_link': post_link,
        'current_year': timezone.now().year,
    })

    email = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
    email.attach_alternative(html_content, "text/html")
    email.send()

def send_group_invite_email(user, group_name, invite_link):
    subject = f"You've been invited to join {group_name}!"
    from_email = 'SIQNet <noreply@siqnet.com>'
    to_email = user.email

    text_content = f"You’ve been invited to join the group '{group_name}' on SIQNet."
    html_content = render_to_string('emails/group_invite.html', {
        'user': user,
        'group_name': group_name,
        'invite_link': invite_link,
        'current_year': timezone.now().year,
    })

    email = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
    email.attach_alternative(html_content, "text/html")
    email.send()

def send_security_alert_email(user, activity_type, location, timestamp):
    subject = "Security Alert: New Activity on Your SIQNet Account"
    from_email = 'SIQNet <security@siqnet.com>'
    to_email = user.email

    text_content = f"New {activity_type} detected from {location} at {timestamp}."
    html_content = render_to_string('emails/security_alert.html', {
        'user': user,
        'activity_type': activity_type,
        'location': location,
        'timestamp': timestamp,
        'current_year': timezone.now().year,
    })

    email = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
    email.attach_alternative(html_content, "text/html")
    email.send()
