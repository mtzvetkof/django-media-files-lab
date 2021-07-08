from django.shortcuts import render, redirect

from phones_media_files.phones.forms import PhoneForm
from phones_media_files.phones.models import Phone


def index(request):
    context = {
        'phones': Phone.objects.all(),
        'form': PhoneForm()
    }

    return render(request, 'index.html', context)


def create_phone(request):
    form = PhoneForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('index')
