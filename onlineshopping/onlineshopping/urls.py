<<<<<<< HEAD
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

=======
"""onlineshopping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

"""onlineshopping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from myshopping import views, urls
from cart import urls
from myshopping.views import displayProductData

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('myshopping.urls')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> 90983e8dfd21e2738962784c2714d34ed62d01db
