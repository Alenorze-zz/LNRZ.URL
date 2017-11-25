from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import View

from .models import LnrzUrl



class LnrzCBView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(LnrzUrl, shortcode=shortcode)
        return HttpResponse("hello again {sc}".format(sc=shortcode))

    def post(self, request, *args, **kwargs):
        return HttpResponse()

