from django.urls import path

from . import views

urlpatterns=[
    path("",views.mainsite),
    path("login",views.log),
    path("logout",views.logout),
    path("register",views.register),
    path("de/<int:pk>",views.dell,name="delete"),
    path("dy/<int:pk>",views.update,name="update"),
    path("dt/<int:pk>",views.showme,name="show"),
    path("dd/<int:pk>",views.sentdata,name="sentdata"),
    path("showcart",views.showcart),
    path("ee",views.emai),
    path("s",views.support),
    path("adminmain",views.shows),
    path("addcollections",views.workbase),
    path("adddata",views.data),
    path("test",views.sentcar)


]