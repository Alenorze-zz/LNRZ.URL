from django.shortcuts import render
from django.http import HttpResponse

def lnrz_redirect_view(request, *args, **kwargs):
    return HttpResponse("Hello")

class LnrzCBView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hell")
