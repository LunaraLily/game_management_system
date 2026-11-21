
from django.contrib import admin
from django.urls import path

from game import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_nug',views.add_nug,name='add_nug'),

    path('del_nug/<int:id>',views.del_nug,name='del_nug'),

    path('edit_nug/<int:id>',views.edit_nug,name='edit_nug'),
]
