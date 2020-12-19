from django.urls import path
from . import views


urlpatterns = [
    path('typelist', views.type_list),
]

