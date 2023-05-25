from django.urls import re_path
from appthree import views

urlpatterns = [
    re_path(r"^$",views.help, name='help'),
]

