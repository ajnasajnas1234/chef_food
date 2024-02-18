from django.urls import path, include
from . import views
from django.contrib import admin
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path("index", views.index,name="index"),
    path("table_reservation",views.table_reservation,name="table_reservation"),
    path("contact_us",views.contact_us,name="contact_us"),
] 