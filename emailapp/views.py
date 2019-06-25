from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.core.mail import EmailMessage
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework import permissions, renderers

from rest_framework.decorators import api_view, permission_classes, action

# Create your views here.
@api_view(['POST'])
@permission_classes((permissions.IsAuthenticated, ))
def eticketing(request):
    # print(request.user)
    if request.method == 'POST':
               
        message = 'Description : {}\nApp Name:{}\nUsername:{}'.format(
            request.POST.get('description', ''),
            request.POST.get('app', ''),
            request.user.username
        )

        mail_subject = request.POST.get('subject', '')
        to_email = 'calcgenamatya@gmail.com'
        email = EmailMessage(mail_subject, message, to=[to_email])
        if request.FILES:
            myfile = request.FILES['pic']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            email.content_subtype = "html"
            email.attach_file('{}/{}'.format(settings.MEDIA_ROOT, filename))
        email.send()
        return JsonResponse({'message': 'We will contact you soon.'})
    else:
        return JsonResponse({'error': '{} method is not available'.format(request.method)})