from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('streaming/', views.StreamingView.as_view(), name='streaming'),
    path('link/', views.LinkView.as_view(), name='link'),
]