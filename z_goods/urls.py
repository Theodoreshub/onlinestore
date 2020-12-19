from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    path('/<string:goodtype>/', views.type_list, name='goodtype'),
]

