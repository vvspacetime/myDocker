from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import RtCatApp
from django.urls import reverse
import logging
from .docker_interface import Docker

logger = logging.getLogger(__name__)
docker = Docker()

def index(request):
    app_list = RtCatApp.objects.all()
    context = {'app_list':app_list}
    return render(request,'hellodocker/index.html',context)

def api(request,app_id):
    count = RtCatApp.objects.count()
    if request.method == "POST":
        newApp = RtCatApp(number=count-1)
        newApp.save()
        docker.create()
        docker.start(num=count - 1)
    elif request.method == "DELETE":
        app = RtCatApp.objects.filter(id=app_id)
        docker.remove(num=app.first().number)
        app.delete()
    return HttpResponse()
