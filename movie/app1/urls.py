from django.contrib import admin
from django.urls import path

from app1 import views

app_name="app1"

urlpatterns = [
    # path('',views.home,name="home"),
    path('',views.Home.as_view(),name="home"),
    # path('add',views.addmovie,name="add"),
    # path('add1',views.addmovie1,name="add1"),
    path('add1',views.Addmovie.as_view(),name="add1"),
    # path('details/<int:m>',views.details,name="details"),
    path('details/<int:pk>',views.Details.as_view(),name="details"),
    # path('delete/<int:m>',views.delete,name="delete"),
    path('delete/<int:pk>',views.Delete.as_view(),name="delete"),
    # path('edit/<int:m>',views.edit,name="edit"),
    path('edit/<int:pk>',views.Edit.as_view(),name="edit"),

]