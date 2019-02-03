from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from userapp.models import User
from rest_framework import status
from django.http import JsonResponse
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny
import json

def SendEmailVerification( user, request):
    current_site = get_current_site(request)
    message = render_to_string('acc_activate_email.html', {
        'username':user.get('username'),
        'domain':current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.get('pk'))).decode(),
        'token': account_activation_token.make_token(user),
    })

    mail_subject = "Activate your account."
    to_email = user.get('email')
    email = EmailMessage(mail_subject,message,to=[to_email])
    email.send()


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
        custom_user = {
            'username':user.username,
            'pk':user.pk,
            'is_active':user.is_active,
            'email':user.email,
        }
    except User.DoesNotExist:
       return JsonResponse({
           'success':'Account cannot be activated'
       })

    if account_activation_token.check_token(custom_user, token):
        user.is_active = True
        user.save()

        return JsonResponse({
            'success':'Account is activated',
        })