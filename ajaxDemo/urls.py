

from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('saveform/', views.saveform, name="saveform"),

]
