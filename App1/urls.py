from django.urls import path
from .views import *

urlpatterns = [
    path('',Home, name="Home"),
    path('palindrome',getPalindrome, name="getpalendrom"),
    path('verify',verifyPalindrome,name='verifyPalindrome'),
    path('register', registerUser, name="registerUser"),
]
