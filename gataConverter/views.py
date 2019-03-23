import os
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.core.files.storage import FileSystemStorage
from gataConverter.converter import Converter

# Create your views here.
def index(request):
    if request.method == 'POST':   
        file = request.FILES['customFile']
        #Converter.checkData(handle_uploaded_file(file))
        return download(file)
   
    return render(request, 'gataConverter/index.html',)

def handle_uploaded_file(file):
    fs = FileSystemStorage()
    print(file.name)
    filename = fs.save(file.name, file)
    uploaded_file_url = fs.url(filename)
    return filename


def download(file):
    print(file.name)
    response = HttpResponse(file, content_type="application/vnd.ms-excel")
    response['Content-Disposition'] = 'inline; filename=' + file.name
    return response