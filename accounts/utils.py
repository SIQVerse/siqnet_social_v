def send_comment_alert_email(user, post_title, comment_link):
    subject = f"New Comment on '{post_title}'"
    from_email = 'SIQNet <noreply@siqnet.com>'
    to_email = user.email

    text_content = f"You received a new comment on '{post_title}'. Click the link to view it."
    html_content = render_to_string('emails/comment_alert.html', {
        'user': user,
        'post_title': post_title,
        'comment_link': comment_link,
        'current_year': timezone.now().year,
    })

    email = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
    email.attach_alternative(html_content, "text/html")
    email.send()
