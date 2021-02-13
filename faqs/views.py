from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Faqs
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import FaqForm


# Create your views here.
def faqs(request):
    """ A view to return all the faqs """

    faqs = Faqs.objects.all()

    context = {
        'faqs': faqs,
    }

    return render(request, 'faqs/faqs.html', context)


@login_required
def add_faq(request):
    """ Add a faq to the site """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store staff can do that!')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = FaqForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added faq!')
            return redirect(reverse('faqs'))
        else:
            messages.error(request, 'Failed to add faq. Please ensure the\
             form is valid.')
    else:
        form = FaqForm()

    template = 'faqs/add_faq.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_faq(request, q_id):
    """ Edit a faq """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store staff can do that!')
        return redirect(reverse('home'))

    faq = get_object_or_404(Faqs, pk=q_id)
    if request.method == 'POST':
        form = FaqForm(request.POST, instance=faq)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated Faq!')
            return redirect(reverse('faqs'))
        else:
            messages.error(request, 'Failed to update Faq. Please ensure\
             the form is valid.')
    else:
        form = FaqForm(instance=faq)

    template = 'faqs/edit_faq.html'
    context = {
        'form': form,
        'faq': faq,
    }

    return render(request, template, context)


@login_required
def delete_faq(request, q_id):
    """ Delete an Faq """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store staff can do that!')
        return redirect(reverse('home'))

    faq = get_object_or_404(Faqs, pk=q_id)
    faq.delete()
    messages.success(request, 'Faq deleted!')
    return redirect(reverse('faqs'))
