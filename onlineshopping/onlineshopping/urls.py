from __future__ import unicode_literals

from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import urls as auth_urls
from .app.views import FooView, SizesView
from django.urls import path
from myshopping.views import displayProductData
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
  
    url(r'^sizes$', SizesView.as_view(), name='sizes'),
    url(r'^', include(auth_urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^ratings/', include('star_ratings.urls', namespace='ratings')),
    path('', include('myshopping.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

