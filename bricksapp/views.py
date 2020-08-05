from django.shortcuts import render, redirect

# Create your views here.
from django.template.loader import render_to_string
from django.core.mail import EmailMessage


def home_view(request):
    return render(request, "index.html", {})


def form_success_view(request):
    budget_range = {'1': '$0 - $2,000', '2': '$2,001 - $5,000', '3': '$5,001 - $10,000', '4': '$10,001 - $15,000',
                    '5': '$15,001 - $20,000', '6': '$20,001 - $30,000', '7': '$30,001 - $40,000',
                    '8': '$40,001 - $50,000',
                    '9': '$50,001 - $60,000', '10': '$60,001 - $70,000', '11': '$70,001 - $80,000',
                    '12': '$80,001 - $100,000',
                    '13': '$100,000+'}
    if request.method == "POST":
        firstname = request.POST.get('FirstName')
        lastname = request.POST.get('LastName')
        email = request.POST.get('Email')
        phonenumber = request.POST.get('PhoneNumber')
        # if phonenumber[0] == '+' and phonenumber[1:].isdigit():
        message = request.POST.get('message')
        courses = request.POST.get('courses')
        budget_id = request.POST.get('Budget')
        request.session['firstname'] = firstname
        request.session['lastname'] = lastname
        request.session['email'] = email
        request.session['phonenumber'] = phonenumber
        request.session['message'] = message
        request.session['courses'] = courses
        request.session['budget'] = budget_range[budget_id]
        # print(firstname, lastname, email, phonenumber, message, budget_range[budget_id])
        mail_subject = 'Contact Details.'
        message = render_to_string('message.html', {'request': request.session})
        to_email = 'mallamspy008@gmail.com'
        email = EmailMessage(
            mail_subject, message, to=[to_email]
        )
        email.send()
        # else:
        #     return redirect('home')
    return render(request, "form_success.html", {})


def visa_embassy_view(request):
    return render(request, "visa-embassy-guidance.html", {})


def airport_pickup_view(request):
    return render(request, "airport-pickup.html", {})


def application_assistance_view(request):
    return render(request, "application-assistance.html", {})


def universities_view(request):
    return render(request, "universities.html", {})