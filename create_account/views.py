from django.shortcuts import render, reverse, redirect
from .forms import AccountForm

from django.contrib import messages


def create_account(request):
    """ A view to return the create account page / form """
    if request.method == 'GET':
        form = AccountForm()
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Sent Account Request')
            return redirect(reverse('home'))
        else:
            messages.error(request, 'Failed to Send Form. Please ensure the\
             form is valid.')
    else:
        form = AccountForm()

    context = {
        'form': form,
    }

    return render(request, 'create_account/create_account.html', context)
