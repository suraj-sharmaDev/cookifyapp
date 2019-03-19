from django.contrib import admin
from . import views

urlpatterns = [
    path('hello/', view.index,name='index'),
]
