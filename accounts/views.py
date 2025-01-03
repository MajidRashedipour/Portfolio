from django.shortcuts import render
from .models import Profile, ContactMe
from .forms import ContactForm


def index(request):
    user = Profile.objects.filter(username='majidrashedipour').first()
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            new_contact = ContactMe(full_name=contact_form.cleaned_data.get('full_name'), email=contact_form.cleaned_data.get('email'), message=contact_form.cleaned_data.get('message'), user=user)
            new_contact.save()
            return render(request, 'accounts/index.html', {'user': user, 'success': 'send message successfully.'})
        else:
            return render(request, 'accounts/index.html', {'user': user,'errors': contact_form.errors})
    else:
        contact_form = ContactForm()
        return render(request, 'accounts/index.html', {'user': user})
