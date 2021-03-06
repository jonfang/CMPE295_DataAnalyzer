from django.urls import path
from analyzer import views

urlpatterns = [
    path("", views.home, name="home"),
    path("submit", views.submit, name="submit"),
    path("case1", views.case1, name="case1"),
    path("case2", views.case2, name="case2"),
    path("case3", views.case3, name="case3"),
    path("report1", views.report1, name="report1"),
    path("report2", views.report2, name="report2"),
    path("report3", views.report3, name="report3"),
    path("report4", views.report4, name="report4"),
    path("report5", views.report5, name="report5"),
    path("report6", views.report6, name="report6"),
]