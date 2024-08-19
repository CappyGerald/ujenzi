from .views import custom_logout_view, signup, user_login
from django.urls import path

app_name = 'register'

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('user_login/', user_login, name='login'),  
    path('logout/', custom_logout_view, name='logout'),
]
