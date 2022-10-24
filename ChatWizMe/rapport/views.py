from django.shortcuts import render
from . import models


def rapport(request):
    context = {
        "text" : models.Report.ma_variable,
        "list" : [1,2,3]
    }
    return render(request, "rapport/rapport.html",context)


