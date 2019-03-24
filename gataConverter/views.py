import os
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from gataConverter.converter import Converter

# Create your views here.
def index(request):
    if request.method == 'POST':   
        file = request.FILES['customFile']
        formats = request.POST.getlist('formatsCheckbox')
        print (formats)
        zipFile = Converter(file,formats).convert()
        return download(zipFile)
   
    return render(request, 'gataConverter/index.html',)


def download(file):
    response = HttpResponse(file, content_type="application/zip")
    response['Content-Disposition'] = 'inline; filename=' + "formated-files.zip"
    return response