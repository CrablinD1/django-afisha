from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from places.views import index, json_place



urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('', index, name='index_page'),
    path('places/<int:id>/', json_place),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
