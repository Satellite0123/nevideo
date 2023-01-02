from django.urls import path
from . import views

app_name = "player"

urlpatterns = [
    # path('', views.MainView.as_view(), name='index'),
    path('player/', views.WatchView.as_view(), name='index'),
]