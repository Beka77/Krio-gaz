from django.urls import path
from apps.users.views import user_register, user_login, account
from django.contrib.auth import views as auth_views  # import this
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('user_register/', user_register, name="user_register"),
    path('user_login/', user_login, name="user_login"),
    path('account/<str:username>', account, name="account"),
    path('logout/', LogoutView.as_view(next_page='index'), name="logout"),
]
