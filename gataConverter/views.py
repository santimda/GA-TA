import os
from django.shortcuts import get_list_or_404, render
from django.http import Http404,HttpResponseRedirect, HttpResponse
from django.template import loader
from gataConverter.converter import Converter
from .models import Downloads
from xlrd import XLRDError
from django.utils.datastructures import MultiValueDictKeyError
from django.urls import reverse

# Create your views here.
def index(request):
    downloads = getDownloads()
    errorMsg = ''
    if request.method == 'POST':  
        try:
            file = request.FILES['customFile']
        except MultiValueDictKeyError:
            errorMsg = "You must choose a file"
        else:
            formats = request.POST.getlist('formatsCheckbox')
            if formats:
                try:
                    Converter(file,formats).convert()
                    downloads.total+=1
                    downloads.save()
                    return render(request, 'gataConverter/index.html', {'downloads': downloads.total,'errorMsg': errorMsg,'isDownload':True})
                except XLRDError:
                    errorMsg = "Incorrect file format, the file must be .xslx or .ods"
                except:
                     errorMsg = "An error occurred during conversion, try again"
            else:
                errorMsg = "You must choose some output format"

    return render(request, 'gataConverter/index.html', {'downloads': downloads.total,'errorMsg': errorMsg,'isDownload':False})

def downloadFile(request):
    try:
        zipFile = Converter().getAndDeleteZipFile()
        response = HttpResponse(zipFile, content_type="application/zip")
        response['Content-Disposition'] = 'inline; filename=' + "converted-files.zip"
        return response
    except FileNotFoundError:
        raise Http404

def sampleFile(request):
    try:
        sampleFile = open("gataConverter/sampleFiles/planilla_generica.xlsx", 'rb')
        response = HttpResponse(sampleFile, content_type="application/vnd.ms-excel")
        response['Content-Disposition'] = 'inline; filename=' + "example-sheet.xlsx"
        return response
    except FileNotFoundError:
        raise Http404

def getDownloads():
    try:
        downloads = get_list_or_404(Downloads)[0]
    except Http404:
        downloads = Downloads(total=0)
        downloads.save()
    return downloads