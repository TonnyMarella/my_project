from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularJSONAPIView, SpectacularSwaggerView
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls'), name='api')
]
if settings.SWAGGER_URL:
    urlpatterns += [
        path('api/v1/Go9lYiNcza68F2lzPrX/', SpectacularAPIView.as_view(), name='schema'),
        path('api/v1/Go9lYiNcza68F2lzPrX.json', SpectacularJSONAPIView.as_view(), name='schema'),
        path(f'{settings.SWAGGER_URL}', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    ]
