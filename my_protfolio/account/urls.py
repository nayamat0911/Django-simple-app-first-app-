from django.urls import path
from .import views

urlpatterns = [
    path('',views.user_log, name = 'login'),
    path('sign_up/', views.sign_up, name = 'sign_up'),
    path('forgot_pasword/',views.forgot_pasword, name = 'forgot_pasword'),
    path('logout/',views.user_logout, name = 'logout'),
]