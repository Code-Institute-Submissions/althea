from django.shortcuts import render
from .models import Contact
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse


def contact_us(request):
    """ View for rendering contact us page"""

    if request.method == "POST":
        if request.POST.get("fname") and request.POST.get("emailadd"):
            post = Contact()
            post.full_name = request.POST.get("fname")
            post.email = request.POST.get("emailadd")
            post.phone_number = request.POST.get("pnumber")
            post.message = request.POST.get("cmessage")
            post.save()

            subject = "Althea Store Inquiry"
            message = post.message = request.POST.get(
                "cmessage") + " From: " + post.full_name + " Sender's Email Address " + post.email + post.phone_number
            from_email = "althea.online.store@gmail.com"
            if subject and message and from_email:
                try:
                    send_mail(
                        subject, message,
                        from_email, ['althea.online.store@gmail.com'])
                except BadHeaderError:
                    return HttpResponse("Invalid Header Found")
                return render(request, "contact/contact_success.html")
            return HttpResponse("Make sure all fields are entered and valid.")
        return render(request, "contact/contact_success.html")
    return render(request, "contact/contact_us.html")
