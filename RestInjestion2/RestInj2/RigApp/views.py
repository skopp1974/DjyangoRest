

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.http import HttpResponse
from .models import Rig
# Create your views here.


# In views.py

def rig_home(request):
    return HttpResponse("Welcome Rig Rigging!!!")

def rig_list(request):
    MAX_OBJECTS = 20
    rigs = Rig.objects.all()[:MAX_OBJECTS]
    data = {"results": list(rigs.values("title"))}#"created_by__username", "pub_date"))}
    return JsonResponse(data)

def rig_detail(request, pk):
    rig1 = get_object_or_404(Rig, pk=pk)
    data = {"results": {
    "question": rig1.title
    # ,
    # "created_by": rig.created_by.username,
    # "pub_date": rig.pub_date
    }}
    return JsonResponse(data)