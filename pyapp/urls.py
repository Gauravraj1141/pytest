from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.homepage),
    path("register", views.User_register, name="register"),
    path("login/", views.User_login, name="login"),
    path("profile/", views.User_profile, name="profile"),
    path("logout/", views.User_logout, name="logout"),
    path("showblog/", views.User_Add_blog, name="showblog"),
    path("readblog/<int:id>/", views.User_read_blog, name="readblog"),
    path("update/<int:id>/", views.User_Update_blog, name="update"),
    path("delete/<int:id>/", views.User_Delete_blog, name="delete"),
    path("about", views.about_blog, name="about"),

]
