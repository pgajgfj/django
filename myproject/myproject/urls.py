from django.contrib import admin
from django.urls import path, include
from usersmovies import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('usersmovies/', include('usersmovies.urls')),  # Для додатка з фільмами
    path('', views.home, name='home'),  # Головна сторінка
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)