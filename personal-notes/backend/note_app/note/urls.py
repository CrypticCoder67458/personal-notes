
from django.urls import path
from note import views

urlpatterns = [

    path('', views.get_notes, name='notes'),
]
