from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest, HttpResponse
from django.views import View
from pathlib import Path

from upload.forms import UploadFile
from django.core.files.storage import FileSystemStorage


# Create your views here.

'''class Upload(View):
    def get(self, request: HttpRequest):
        form = UploadFile()
        return render(request, 'upload/upload.html', locals())

    def post(self, request: HttpRequest):
        file = open('.\static\\read.txt', 'r')
        data = file.read()
        file.close()
        context = {'data': data.strip(), 'len': len(data)}
        return render(request, 'upload/showfile.html', context)'''


class Upload(View):
    def get(self, request: HttpRequest):
        return render(request, 'upload/upload.html', locals())

    def post(self, request: HttpRequest):
        if request.method == 'POST':
            upload_file = request.FILES['document']
            fs = FileSystemStorage()
            fs.save(upload_file.name, upload_file)
            path = Path("media/")
            extension = ".txt"
            file_with_extension = next(path.glob(f"*{extension}"))
            if file_with_extension:
                with open(file_with_extension) as file:
                    data = file.read()
                    context = {'data': data.strip(), 'len': len(data)}
                    return render(request, 'upload/showfile.html', context)
