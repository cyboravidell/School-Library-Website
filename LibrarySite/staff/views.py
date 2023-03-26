from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from .models import Home,AboutCorousel
# Create your views here.

def staff(request):
    homecontent = Home.objects.all()
    aboutCorousel = AboutCorousel.objects.all()
    
    abt = list()
    for i in aboutCorousel:
        abt.append([i.image,i.position])
    abt.sort(key=lambda x: x[1])

    
    print(list(aboutCorousel))
    context = {'homecontent' : homecontent,
               'aboutCorousel':abt}
    print(homecontent)
    return render(request, "staff.html", context)

def edit_home(request):
    if request.method == 'POST':
        uploaded_file = request.FILES.get('image')
        line1 = request.POST['line1']
        line2 = request.POST['line2']
        line3 = request.POST['line3']
        print(uploaded_file)
        if uploaded_file is not None:
            fs = FileSystemStorage(location='static/uploads/home')
            fs.save(uploaded_file.name, uploaded_file)
            home = get_object_or_404(Home,Sno=1)
            home.image = uploaded_file.name
            home.line_1 = line1
            home.line_2 = line2
            home.line_3 = line3
            home.save()
            messages.success(request, "Home Section Editted Successfully")
        else:
            messages.error(request, "Invalid file type choosen, Please try again with correct file type")
        return redirect('staff')
    else:
        return render(request, 'staff.html')
        

def edit_aboutCorousel(request):
    if request.method == "POST":
        uploaded_file = request.FILES.get('image')
        lpos=request.POST['lpos']
        lastimage=request.POST['lastimage']
        npos=request.POST['npos']
        if uploaded_file is not None:
            fs = FileSystemStorage(location='static/uploads/about')
            fs.save(uploaded_file.name, uploaded_file)
            try:
                about = get_object_or_404(AboutCorousel,position=lpos,image = lastimage)
                about.image=uploaded_file.name
                about.position=npos
                about.save()
                messages.success(request, "Selected Corousel Modified Successfully")
            except:
                print("exception occured")
                messages.error(request, "There are multiples data found with same Image position please check that and try again")
            return redirect('staff')

        else:
            messages.error(request, "Invalid file type choosen, Please try again with correct file type")
        return redirect('staff')
    else:
        return render(request, 'staff.html')


def delete_about_corousel(request):
    if request.method == 'POST':
        try:
            corousel_id = request.POST.get('corousel_id')
            lastimage=request.POST['lastimage']
            corousel = AboutCorousel.objects.get(position=corousel_id,image = lastimage)
            print(corousel)
            corousel.delete()
            messages.success(request, "Selected Corousel Deleted Successfully")
            return redirect('staff')

        except:
            messages.error(request, "There are multiples data found with same Image position please check that and try again")
            return redirect('staff')
    else:
        return render(request, 'staff.html')



    