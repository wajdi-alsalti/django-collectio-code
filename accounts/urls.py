from django.urls import path, include

from . import views

app_name = 'accounts'

urlpatterns = [
    # path('log-out',views.logout_view,name='log-out'),
    path('signup',views.signUp,name='signup'),
    path('profile/',views.profileUser,name='profile'),
    path('profileEdit',views.profileEdit,name='profileEdit'),
]
