from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_view

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^catalog/', include('catalog.urls')),
    url(r'^$', RedirectView.as_view(url='/catalog/', permanent=True)),    # Read about RedirectView
    url(r'^imagefit/', include('imagefit.urls')),

    # User Related urls
    # url(r'^users/logout/$', auth_view.logout, name='auth_logout'),
    # url(r'^register/complete/$', RedirectView.as_view(pattern_name='index'), name='registration_complete'),
    #
    url(r'^accounts/', include('registration.backends.default.urls')),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
