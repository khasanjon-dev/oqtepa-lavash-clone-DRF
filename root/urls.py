from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from root import settings

schema_view = get_schema_view(
    openapi.Info(
        title="Oqtepa Lavash API",
        default_version='v1',
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="khasanjon.dev@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)

urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='swagger'),
    path('admin/', admin.site.urls),
    path('api/', include('apps.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
