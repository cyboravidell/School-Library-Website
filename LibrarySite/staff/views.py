from django.shortcuts import render, redirect, HttpResponse
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from .models import Home
# Create your views here.

def staff(request):
    homecontent = Home.objects.all()

    context = {'homecontent' : homecontent}
    print(homecontent)
    return render(request, "staff.html", context)

def edit_home(request):
    if request.method == 'POST':
        uploaded_file = request.FILES.get('image')
        print(uploaded_file)
        if uploaded_file is not None:
            fs = FileSystemStorage(location='static/uploads/home')
            fs.save(uploaded_file.name, uploaded_file)
            messages.success(request, "Successfully Uploaded")
        else:
            messages.error(request, "Invalid file type choosen, Please try again with correct file type")
        return redirect('staff')
    else:
        return render(request, 'staff.html')
        
    