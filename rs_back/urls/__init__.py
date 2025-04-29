from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView

API_PREFIX = 'api'


urlpatterns = [
    path('admin/', admin.site.urls),
    path(API_PREFIX + '/v0/', include('rs_back.urls.v0')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__', include(debug_toolbar.urls)),
        path(API_PREFIX + '/schema/', SpectacularAPIView.as_view(), name='schema'),
        path(API_PREFIX + '/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger')
    ]

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
