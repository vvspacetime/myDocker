from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import RtCatApp
from django.urls import reverse
import logging


logger = logging.getLogger(__name__)

def index(request):
    app_list = RtCatApp.objects.all()
    context = {'app_list':app_list}
    return render(request,'hellodocker/index.html',context)

def api(request,app_id):
    if request.method == "POST":
        newApp = RtCatApp()
        newApp.save()
    elif request.method == "DELETE":
        RtCatApp.objects.filter(id = app_id).delete()
    return HttpResponse()

def deleteApp(request):
    return HttpResponseRedirect(reverse('hellodocker:index'))

def addApp(request):
    return HttpResponseRedirect(reverse('hellodocker:index'))