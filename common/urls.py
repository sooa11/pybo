from django.urls import path
from django.contrib.auth import views as auth_views
from .import views

app_name ='common'

urlpatterns = [
    # path('login/', auth_views(), name='login'), 아래로 수정하여서 사용하지 않음
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
]