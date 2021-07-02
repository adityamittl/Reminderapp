from django.urls import path
from .views import signin,signup,signout

urlpatterns = [
    path('login/',signin),
    path('signup/',signup),
    path('signout/', signout),
]
