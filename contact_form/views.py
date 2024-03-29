from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from .forms import ContactForm


def contact(request):
    """ 
    a view to display a email form and to send the email
    also to show a google map and contact info.
    """
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = render_to_string(
                'contact_form/emails/subject.txt',
                {'sender_email': form.cleaned_data['from_email'],
                 'subject': form.cleaned_data['subject']})
            body_text = render_to_string(
              'contact_form/emails/body.txt',
              {'sender_email': form.cleaned_data['from_email'],
               'subject': form.cleaned_data['subject'],
               'message': form.cleaned_data['message']})
            body = render_to_string(
              'contact_form/emails/body.html',
              {'sender_email': form.cleaned_data['from_email'],
               'subject': form.cleaned_data['subject'],
               'message': form.cleaned_data['message']})
            from_email = form.cleaned_data['from_email']
            try:
                send_mail(subject, body_text, from_email,
                          ['tom@wilson-express.co.uk'], html_message=body)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, 'contact_form/contact_form.html', {'form': form})


def success(request):
    """ 
    the same as the contact view except it displays a success message 
    """
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email,
                          ['admin@wilsons-express.co.uk'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, 'contact_form/success.html', {'form': form})
