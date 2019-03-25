import os
from django.shortcuts import get_list_or_404, render
from django.http import Http404,HttpResponseRedirect, HttpResponse
from django.template import loader
from gataConverter.converter import Converter
from .models import Downloads
from xlrd import XLRDError

# Create your views here.
def index(request):
    try:
        downloads = get_list_or_404(Downloads)[0]
    except Http404:
        downloads = Downloads(total=0)
        downloads.save()
    errorMsg = ''
    if request.method == 'POST':   
        file = request.FILES['customFile']
        formats = request.POST.getlist('formatsCheckbox')
        if formats:
            print (formats)
            try:
                zipFile = Converter(file,formats).convert()
                downloads.total+=1
                downloads.save()
                return download(zipFile)
            except XLRDError:
                errorMsg = "Formato de archivo incorrecto, el archivo debe ser .xslx o .ods"
        else:
            errorMsg = "Debe elegir algún formato de salida"

    return render(request, 'gataConverter/index.html', {'downloads': downloads.total,'errorMsg': errorMsg})


def download(file):
    response = HttpResponse(file, content_type="application/zip")
    response['Content-Disposition'] = 'inline; filename=' + "formated-files.zip"
    return response