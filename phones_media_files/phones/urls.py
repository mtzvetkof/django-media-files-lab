from django.urls import path

from phones_media_files.phones.views import index

urlpatterns = [
    path('', index, name='index')
]