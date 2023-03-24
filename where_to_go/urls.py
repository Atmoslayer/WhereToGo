from django.contrib import admin
from django.urls import path
from map_poster import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show_main)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
