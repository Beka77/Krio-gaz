from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from apps.settings.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('', include('apps.settings.urls')),
    path('users/', include('apps.users.urls')),

] 

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)