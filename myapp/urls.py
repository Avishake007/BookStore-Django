from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
   path("", views.index, name="myapp"),
   path("addBook",views.addBook,name="addBook"),
   path("viewBook/<str:pk>",views.viewBook,name="viewBook"),
   path("updateBook/<str:pk>",views.updateBook,name="updateBook"),
   path("deleteBook/<str:pk>",views.deleteBook,name="deleteBook"),
   path("register", views.registerUser, name = "register"),
   path("login",views.loginUser, name="login"),
   path("logout", views.logoutUser, name = "logout")
    
]
