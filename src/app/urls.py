from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings

schema_view = get_schema_view(
    openapi.Info(
        title="Example Middleware - API",
        default_version='v1',
        description="Api service example SBTUR",
    ),
    public=False,
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=None), name='schema-swagger-ui'),
    path('docs/', schema_view.with_ui('redoc', cache_timeout=None), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]

if settings.DEBUG:
	import debug_toolbar

	urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]
