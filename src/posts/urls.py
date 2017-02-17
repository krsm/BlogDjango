from django.conf.urls import url
from django.contrib import admin

from .views import (
    post_list,
    post_create,
    post_detail,
    post_update,
    post_delete,
    post_create,
)

# it could be done a different approach
# Using Function Views
urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # custom urls
    # $ indicates end of regex
    url(r'^$', post_list),
    url(r'^create/$', post_create),
    # name added to url, then the name added can be used on the templates
    url(r'^(?P<id>\d+)/$', post_detail, name='detail'),
    url(r'^(?P<id>\d+)/edit/$', post_update, name='update'),
    url(r'^delete/$', post_delete),
    # url(r'^create/$', post_create),
    # generic
    # url(r'^url_app/$', "<appname>.views.<function_name),
]
