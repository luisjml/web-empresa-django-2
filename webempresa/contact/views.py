from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage

# Create your views here.

def contact(request):
    contact_form = ContactForm

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid:
            name = request.POST.get("name","")
            email = request.POST.get("email","")
            content = request.POST.get("content","")
            #Enviamos el correo y redireccionamos
            #email=EmailMessage(asunto, cuerpo, email_origen, email_destino, reply_to=[email])
            email=EmailMessage(
                "La Cafettiera: Nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribió:\n\n{}".format(email,name,content),
                "no-contestar@inbox.mailtrap.io",
                ["ljmarchli@gmail.com"],
                reply_to=[email]
            )
            try:
                email.send()
                #todo ha ido bien, redirigimos a OK
                return redirect(reverse("contact")+"?ok")
            except:
                #algo no ha ido bien, redirigimos a FAIL
                return redirect(reverse("contact")+"?fail")

            return redirect(reverse("contact")+"?ok")

    return render(request, "contact/contact.html",{'form':contact_form})

