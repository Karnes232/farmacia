from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create", views.create, name="create"),
    path("services", views.services, name="services"),
    path("COGS", views.cogs, name="cogs"),
    path("report", views.report, name="report"),
    path("blog", views.blog, name="blog"),
    path("about", views.about, name="about"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),

]