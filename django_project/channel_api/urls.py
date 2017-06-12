from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from channel_api.views import group_views

__author__ = 'Muhammad Anis <anis@kartoza.com>'
__date__ = '10/06/17'

urlpatterns = [
    url(r'^group', group_views.GroupAPI.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
