from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
import account.urls
import deliver.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(account.urls)),
    path('', include(deliver.urls)),

]

urlpatterns += [
        path('api-auth/', include('rest_framework.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
