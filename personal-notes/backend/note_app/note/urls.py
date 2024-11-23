
from django.urls import path
from note import views

urlpatterns = [

    path('notes/', views.notes, name='notes'),        
    path('notes/<int:id>', views.note_detail, name='note'),

]
