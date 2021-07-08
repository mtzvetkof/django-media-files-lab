from django.shortcuts import render

from phones_media_files.phones.models import Phone


def index(request):
    context = {
        'phones': Phone.objects.all(),
    }

    return render(request, 'index.html', context)