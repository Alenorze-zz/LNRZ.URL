from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View

from .forms import SubmitUrlForm
from .models import LnrzUrl


class HomeView(View):
    def get(self, request, *args, **kwargs):
        the_form = SubmitUrlForm()
        context = {
            "title": "LNRZ.co",
            "form": the_form
        }
        return render(request, "shortener/home.html", {})

    def post(self, request, *args, **kwargs):
        form = SubmitUrlForm(request.POST)
        if form.is_valid():
            print(form.cleaned.data)
        context = {
            "title": "LNRZ.co",
            "form": form
        }
        return render(request, "shortener/home.html", {})

class LnrzCBView(View): #class based view
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(LnrzUrl, shortcode=shortcode)
        return HttpResponseRedirect(obj.url)