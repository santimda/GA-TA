import os
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.core.files.storage import FileSystemStorage

# Create your views here.
def index(request):
    if request.method == 'POST':   
        file = request.FILES['customFile']
        handle_uploaded_file(file)
        return download(file.name)
   
    return render(request, 'gataConverter/index.html',)

def handle_uploaded_file(file):
    fs = FileSystemStorage()
    print(file.name)
    filename = fs.save(file.name, file)
    uploaded_file_url = fs.url(filename)

def download(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404