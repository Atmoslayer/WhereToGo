from django.contrib import admin
from django.urls import path
from map_poster import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show_main)
]
