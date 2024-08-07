from django.urls import path
from test_app import views

urlpatterns = [
    path('', views.display_map, name='display_map')
]