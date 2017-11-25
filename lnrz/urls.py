from django.conf.urls import url
from django.contrib import admin

from shortener.views import lnrz_redirect_view, LnrzCBView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^a/(?P<shortcode>[\w-]+)/$', lnrz_redirect_view),
    url(r'^b/(?P<shortcode>[\w-]+)/$', LnrzCBView.as_view()),
]
