from django.urls import path
from . import views


urlpatterns: list = [
    path('', views.simple_view),
    path('testcall/', views.test_api_call, name='testapicall'),
    path('ff6/bestiary/<int:enemy_number>', views.ffvi_bestiary, name="ff6bestiary")
]

