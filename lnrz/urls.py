from django.conf.urls import url
import django.contrib import admin

from shortener.views import lnrz_redirect_view, LnrzCBView

urlpatterns = [
    url(r'^admin/', admin.site.url),
    url(r'^view-1/', lnrz_redirect_view),
    url(r'^view-2/', LnrzCBView.as_view()),
]
