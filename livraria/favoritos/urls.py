from django.urls import path

from . import views

urlpatterns = [
    path('addfav/<int:livros_id>', views.addfav, name='addfav'),
    path('deletelivro/<int:id>', views.deletelivro, name='deletelivro')
    
]
