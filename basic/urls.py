from django.urls import path, include
from . import views

app_name = 'basic'

urlpatterns = [
    path('',views.home, name = 'home'),
    path('<str:url_title>', views.detail, name = 'detail')
]
