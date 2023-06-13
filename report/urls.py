from django.urls import path
from . import views

urlpatterns = [
    path('', views.city_list, name='city_list'),
    # path('date/', views.datetimepicker_view, name='date'),
]
