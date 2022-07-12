from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from .forms import ContactForm, CareerForm



def home(request):
        if request.method == 'POST':
            form = ContactForm(request.POST)

            if form.is_valid():
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                content = form.cleaned_data['content']

                html = render_to_string('design/contact_form.html', {
                    'name': name,
                    'email': email,
                    'content': content
                })

                send_mail('The contact form subject', 'This is the message', 'alfitori709@gmail.com', ['alfitori.monder@gmail.com'], html_message=html)

                return redirect('contact')
        else:
            form = ContactForm()
        return render(request, 'design/home.html', {'form': form})


def about(request):
    return render(request, 'design/about.html', {})


def contact(request):
        if request.method == 'POST':
            form = ContactForm(request.POST)

            if form.is_valid():
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                content = form.cleaned_data['content']

                html = render_to_string('design/contact_form.html', {
                    'name': name,
                    'email': email,
                    'content': content
                })

                send_mail('The contact form subject', 'This is the message', 'alfitori709@gmail.com', ['alfitori.monder@gmail.com'], html_message=html)

                return redirect('contact')
        else:
            form = ContactForm()
        return render(request, 'design/contact.html', {'form': form})


def career(request):
    return render(request, 'design/career.html', {})

def career_detail(request):
        if request.method == 'POST':
            form = CareerForm(request.POST)

            if form.is_valid():
                fname = form.cleaned_data['fname']
                lname = form.cleaned_data['lname']
                age = form.cleaned_data['age']
                phone = form.cleaned_data['phone']
                email = form.cleaned_data['email']
                content = form.cleaned_data['content']

                html = render_to_string('design/career_detail_form.html', {
                    'fname': fname,
                    'lname': lname,
                    'age': age,
                    'email': email,
                    'phone': phone,
                    'content': content,
                })

                send_mail('The Career form', 'This is the message', 'alfitori709@gmail.com', ['alfitori.monder@gmail.com'], html_message=html)

                return redirect('career_detail')
        else:
            form = CareerForm()
        return render(request, 'design/Career_detail.html', {'form': form})



def services(request):
    return render(request, 'design/services.html', {})



def consulting_services(request):
    return render(request, 'design/consulting_services.html', {})