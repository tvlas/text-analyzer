from django.urls import path
from .views import Upload
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path(
        'loadfile/',
        Upload.as_view(),
        name='upload-file',
    )
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)