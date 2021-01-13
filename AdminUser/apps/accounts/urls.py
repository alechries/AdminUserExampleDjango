from django.urls import path
from .decorators import check_recaptcha
from .views import SignUp

urlpatterns = [
    path('signup/', check_recaptcha(SignUp.as_view()), name='signup'),
]