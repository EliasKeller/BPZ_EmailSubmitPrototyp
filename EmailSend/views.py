from django.shortcuts import render
from django.http import BadHeaderError, HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail


def index(request):
    send_mail('Test-Mail', 'Hello there...;)',
              'elias.keller@gmail.com',
              ['rixuzixova@mail-hub.info'],
              fail_silently=False)
    return render(request, 'tent/index.html')
