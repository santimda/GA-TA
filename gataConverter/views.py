import os
from django.shortcuts import get_list_or_404, render
from django.http import Http404,HttpResponseRedirect, HttpResponse
from django.template import loader
from gataConverter.converter import Converter
from .models import Downloads
from xlrd import XLRDError
from django.utils.datastructures import MultiValueDictKeyError
from django.urls import reverse
import logging

# Create your views here.
def index(request):
    logger = getAppLogger()
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
                    logger.info("[INFO]: file converted")
                    downloads.total+=1
                    downloads.save()
                    return render(request, 'gataConverter/index.html', {'downloads': downloads.total,'errorMsg': errorMsg,'isDownload':True})
                except XLRDError as error:
                    logger.error("[ERROR]: ")
                    logger.exception(error)
                    errorMsg = "Incorrect file format, the file must be .xslx or .ods"
                except Exception as error:
                    logger.error("[ERROR]: " )
                    logger.exception(error)
                    errorMsg = "An error occurred during conversion, try again"
            else:
                errorMsg = "You must choose some output format"

    return render(request, 'gataConverter/index.html', {'downloads': downloads.total,'errorMsg': errorMsg,'isDownload':False})

def downloadFile(request):
    logger = getAppLogger()
    try:
        zipFile = Converter().getAndDeleteZipFile()
        response = HttpResponse(zipFile, content_type="application/zip")
        response['Content-Disposition'] = 'inline; filename=' + "converted-files.zip"
        logger.info("[INFO]: zip downloaded")
        return response
    except FileNotFoundError:
        raise Http404

def sampleFile(request):
    logger = getAppLogger()
    try:
        sampleFile = open("gataConverter/sampleFiles/generic_table.xlsx", 'rb')
        response = HttpResponse(sampleFile, content_type="application/vnd.ms-excel")
        response['Content-Disposition'] = 'inline; filename=' + "example-sheet.xlsx"
        logger.info("[INFO]: Sample file downloaded")
        return response
    except FileNotFoundError:
        raise Http404

def manual(request):
    logger = getAppLogger()
    try:
        sampleFile = open("gataConverter/sampleFiles/manual.pdf", 'rb')
        response = HttpResponse(sampleFile, content_type="application/pdf")
        response['Content-Disposition'] = 'inline; filename=' + "manual.pdf"
        logger.info("[INFO]: Manual downloaded")
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

def getAppLogger():
    return logging.getLogger("gata-logger")
