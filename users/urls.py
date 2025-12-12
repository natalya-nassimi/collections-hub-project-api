from django.urls import path
from .views import SignUpView, SignInView, MeView

urlpatterns = [
    path('sign-up/', SignUpView.as_view()),
    path('sign-in/', SignInView.as_view()),
    path('me/', MeView.as_view())
]