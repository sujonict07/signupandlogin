from django.urls import path
from .views import SignUp, signup


urlpatterns = [
    path('signup/', signup, name='signup'),
]