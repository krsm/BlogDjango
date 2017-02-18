"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin

# Serving static files during development
from django.conf import settings
from django.conf.urls.static import static


# it could be done a different approach
# Using Function Views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # custom urls
    # $ indicates end of regex
    url(r'^posts/', include("posts.urls", namespace='posts')),
    # namespace should be used when there are a set of urls,
    # for instance /posts/create/
    # /posts/delete/
    # /posts/update/
    # generic
    # url(r'^url_app/$', "<appname>.views.<function_name),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
