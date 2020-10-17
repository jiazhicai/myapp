from django.shortcuts import render
from appdata.models import AllBaseInfo
# from appdata import models
from django.shortcuts import HttpResponseRedirect, HttpResponse, render
# Create your views here.


def table(request):
    response1 = ""
    # name = models.name()
    users = AllBaseInfo.objects.all()
    # for user in users:
    #     response1 += user.name + " "
    # return HttpResponse(users)
    return render(request, "table.html", {"data": users})
