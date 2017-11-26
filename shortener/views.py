from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import LnrzUrl


def test_view(request):
    return HttpResponse("some stuff")

def lnrz_redirect_view(request, shortcode=None, *args, **kwargs): #function based view FBV
    obj = get_object_or_404(LnrzUrl, shortcode=shortcode)
    return HttpResponseRedirect(obj.url)



class LnrzCBView(View): #class based view
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(LnrzUrl, shortcode=shortcode)
        return HttpResponseRedirect(obj.url)

    def post(self, request, *args, **kwargs):
        return HttpResponse()