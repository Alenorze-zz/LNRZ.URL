from django.conf.urls import url
from django.contrib import admin

from shortener.views import lnrz_redirect_view, LnrzCBView, test_view

urlpatterns = [
    url(r'^about123/$', test_view),
    url(r'^(?P<shortcode>[\w-]+){6,15}/$', lnrz_redirect_view),
    url(r'^b/(?P<shortcode>[\w-]+){6,15}/$', LnrzCBView.as_view()),
]
