from django.shortcuts import render
from appdata.models import FinallPageDatas
# from appdata import models
from django.shortcuts import HttpResponseRedirect, HttpResponse, render
# Create your views here.
import json

def table(request):
    response1 = ""
    # name = models.name()
    data = FinallPageDatas.objects.all()
    data = data.values()
    data = list(data)
    # for user in users:
    #     response1 += user.name + " "
    # return HttpResponse(users)
    # return render(request, "table.html", {"data": users})
    return HttpResponse(json.dumps(data), content_type="application/json")

