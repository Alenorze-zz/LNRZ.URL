from django.conf.urls import url
from django.contrib import admin

from shortener.views import LnrzCBView, HomeView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view()),
    url(r'^b/(?P<shortcode>[\w-]+)/$', LnrzCBView.as_view(), name='scode'),
]
