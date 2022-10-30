from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator as token_generator


def send_email_to_verify(request, user, use_https=True):
    current_site = get_current_site(request)
    context = {
        'domain': current_site.domain,
        'site_name': current_site.name,
        'user': user,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': token_generator.make_token(user),
        'protocol': 'https' if use_https else 'http',
    }
    message = render_to_string('users/verify_email.html', context=context)
    email = EmailMessage('Verify Email', message, to=[user.email])
    email.send()