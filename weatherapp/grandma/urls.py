from django.urls import path
from grandma import views

app_name = 'grandma'

urlpatterns = [
    path('', views.index, name='index'),
]
