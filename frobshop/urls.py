from django.apps import apps
from django.urls import include, path
from django.contrib import admin
from django.views.static import serve
from frobshop import settings
urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),

    # The Django admin is not officially supported; expect breakage.
    # Nonetheless, it's often useful for debugging.

    path('admin/', admin.site.urls),
    path(r'media/?P<path>.*',serve,{"document_root":settings.MEDIA_ROOT}),

    path('', include(apps.get_app_config('oscar').urls[0])),
]
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
