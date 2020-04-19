from django.shortcuts import render
from .forms import *
from .models import *
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site


# Create your views here.


def base(request):
    port=portfolio.objects.all()

    # print(images[0].image)
    form=contactForm()
    if request.method=='POST':
        # print(request.POST)
        current_site = get_current_site(request)
        form=contactForm(request.POST, request.FILES)
        if form.is_valid():
            message = render_to_string('email.html', {
                'user':request.POST['Name'], 'domain':current_site.domain,
                'email':request.POST['Email'],'subject':request.POST['Subject'],
                'message':request.POST['Message']
            ,
            })
            mail_subject = 'You have got a contact'
            to_email = 'dawarsardar786@gmail.com'
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            form.save()

            context=  {
                'form' : contactForm(),
                'show_pop' : True,
                'port':port

            }
            return render(request, 'base.html', context)
    context = {
        'form':form,
        'show_pop' : False,
        'port':port
    }
    return render(request,'base.html',context)
