from django.urls import path
from analyzer import views

urlpatterns = [
    path("", views.home, name="home"),
    path("report1", views.report1, name="report1"),
    path("report2", views.report2, name="report2"),
    path("report3", views.report3, name="report3"),
]