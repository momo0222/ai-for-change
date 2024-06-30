from django.urls import path

from .views import SignUpView, profile_edit

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile-edit/', profile_edit, name='profile')
]