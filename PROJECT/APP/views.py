from django.shortcuts import render
from .models import Image
from django.http import HttpResponse
# Create your views here.
def add_image(request):
    if request.method=='POST':
        photo1 = request.FILES.get('photo')
        sign1 = request.FILES.get('sign')
        file1= request.FILES.get('resume')

        if photo1 and sign1:
            img = Image(photo=photo1,sign=sign1, resume=file1)
            img.save()

            return HttpResponse("Photo added successfully!")

        return HttpResponse("Error: All fields are required!", status=400)
    return render(request,'add.html')



def view_image(request):
    im=Image.objects.all()
    return render(request,'view.html',{'var':im})
