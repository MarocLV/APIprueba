from django.urls import path

from .views import UsuarioView, CustomUserView


urlpatterns = [   
path('register/',UsuarioView.as_view()),
path('registered/',CustomUserView.as_view({'get': 'list'}))
]