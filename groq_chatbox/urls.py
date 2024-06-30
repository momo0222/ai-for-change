from django.urls import path
from .views import school_chat, mentalhalth_chat, match_with_others

urlpatterns = [
    path('school/', school_chat, name='school'),
    path('mental_health/', mentalhalth_chat, name='mental_health'),
    path('matches/', match_with_others, name='match'),
]
