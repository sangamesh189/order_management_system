from django.urls import path
from .views import login_token_view,register_view,get_profile,update_profile
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('login/',login_token_view.as_view(),name='login'),
    path('register/',register_view.as_view(),name='register'),
    path('profile/',get_profile,name = 'profile'),
    path('profile/update/',update_profile,name='update-profile'),
    path('login/refresh/',TokenRefreshView.as_view(),name='token_refresh')
]