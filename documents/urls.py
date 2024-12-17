from django.urls import path
from . import views

urlpatterns = [path('', views.index, name='index'),

               path('reader/<str:instance_id>', views.create_reader, name='book'),
                path('create/book/<str:instance_id>', views.insert_book, name='book'),
               path('delete/reader/<str:instance_id>', views.delete_reader, name='book'),
               path('delete/book/<str:instance_id>', views.delete_book, name='book'),
               ]
