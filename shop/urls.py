from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index ,name = "shophome" ),
    path("about/", views.about ,name = "Aboutus" ),
    path("contact/", views.contact ,name = "contactus" ),
    # path("track/", views.track1,name = "tracking" ),
      path("products/<int:myid>", views.productView, name="ProductView"),
    path("search/", views.search,name = "search" ),
    path("checkout/" , views.checkout, name = "checkout"),
]