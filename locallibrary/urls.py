from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_view

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # Social auth
    url(r'', include('social_django.urls', namespace='social')),
    url(r'^catalog/', include('catalog.urls')),
    url(r'^$', RedirectView.as_view(url='/catalog/', permanent=True)),    # Read about RedirectView
    url(r'^imagefit/', include('imagefit.urls')),

    url(r'^accounts/', include('registration.backends.default.urls')),


]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
