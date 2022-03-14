from django.shortcuts import render
from django.http import HttpRequest
from django.views import View
from pathlib import Path
from django.core.files.storage import FileSystemStorage


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
                with open(file_with_extension, encoding='utf8') as file:
                    data = file.read()
                    context = {'data': data.strip(), 'len': len(data)}
                    file.close()
                    fs.delete(upload_file.name)
                    return render(request, 'upload/showfile.html', context)
