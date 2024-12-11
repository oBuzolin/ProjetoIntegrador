from django.urls import path
from .views import login_view, reset_password, reset_password_success

urlpatterns = [
    path('', login_view, name='login'),
    path('reset/', reset_password, name='reset'),
    path('reset/success/', reset_password_success, name='reset_sucess'),
    # outras URLs do seu aplicativo
]

