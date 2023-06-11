from django.shortcuts import render,redirect
from apps.settings.models import Setting, Contact
from django.core.mail import send_mail
# Create your views here.
def index(request):
    setting = Setting.objects.latest('id')
    context = {
        'setting' : setting,
    }
    return render (request, 'index.html', context) 

def gallery(request):
    setting = Setting.objects.latest('id')
    context = {
        'setting' : setting
    }
    return render(request, 'pages/gallery.html', context)

def contact(request):
    setting = Setting.objects.latest('id')
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = Contact.objects.create(name = name, email = email, message = message,)
        send_mail(
                    # title:
                    f"{setting.title}",
                    # message:
                    f"{name} спасибо за ваше сообщение. В скором времени мы вам ответим. Ваше сообщение: {message}",
                    # from:
                    "support@gmail.com",
                    # to:
                    [email]
            )
        return redirect('index')
    context = {
        'setting' : setting
    }
    return render (request,'pages/full-width.html', context) 

def basic_grid(request):
    setting = Setting.objects.latest('id')
    context = {
        'setting' : setting
    }
    return render(request, 'pages/basic-grid.html', context)