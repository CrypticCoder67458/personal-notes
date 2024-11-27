
from django.urls import path
from note import views

urlpatterns = [

    path('', views.notes, name='notes'),        
    path('<int:id>/', views.note_detail, name='note'),

]
