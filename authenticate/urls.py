from django.urls import path
from .views import signin,signup,signout
from data.views import complete_profile
urlpatterns = [
    path('login/',signin),
    path('signup/',signup),
    path('signout/', signout),
    path('complete-profile',complete_profile),
]
