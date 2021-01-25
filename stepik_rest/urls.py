from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include

from stepik_rest import settings

api_url = [
    path('item/', include('items.urls'))
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(api_url))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
