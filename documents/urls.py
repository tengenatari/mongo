from django.urls import path
from . import views

urlpatterns = [path('<str:instance>', views.index, name='index'),

               path('<str:instance>/<str:instance_id>', views.create_reader, name='book'),
               path('delete/<str:instance>/<str:instance_id>', views.delete_reader, name='book'),
               path('create/attribute/<str:instance>/<str:instance_id>', views.add_attribute, name='attribute'),
               ]
