from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from .models import Home,AboutCorousel,AboutText,AboutLibrarian,BooksNewArrival,BooksTopPicks
# Create your views here.

def staff(request):
    
    homecontent = Home.objects.all()
    aboutCorousel = AboutCorousel.objects.all()
    aboutPatron = AboutLibrarian.objects.get(Sno = 1)
    aboutlibrarian = AboutLibrarian.objects.get(Sno = 2)
    booksNewArrival = BooksNewArrival.objects.all()
    booksTopPicks = BooksTopPicks.objects.all()
    
    abt = list()
    for i in aboutCorousel:
        abt.append([i.image,i.position])
    abt.sort(key=lambda x: x[1])

    bna = list()
    for i in booksNewArrival:
        bna.append([i.image,i.position])
    bna.sort(key=lambda x: x[1])

    btp = list()
    for i in booksTopPicks:
        btp.append([i.image,i.position])
    btp.sort(key=lambda x: x[1])

    
    print(list(aboutCorousel))
    context = {'homecontent' : homecontent,
               'aboutCorousel':abt, 'aboutPatron':aboutPatron, 'aboutlibrarian':aboutlibrarian, 'booksNewArrival': bna, 'booksTopPicks': btp}
    
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
                print("ediited")
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
        
        corousel_id = request.POST.get('corousel_id')
        lastimage=request.POST['lastimage']
        print(lastimage,corousel_id)
        corousel = AboutCorousel.objects.get(position=corousel_id,image = lastimage).delete()
        messages.success(request, "Selected Corousel Deleted Successfully")
        return redirect('staff')    

    
    else:
        return render(request, 'staff.html')
    
def edit_aboutText(request):
    if request.method == 'POST':
        ntext = request.POST.get('ntext')
        aboutText = get_object_or_404(AboutText,Sno=1)
        aboutText.text = ntext
        aboutText.save()
        messages.success(request, "About Section Text Updated Succesfully")
        return redirect('staff')    
    
    else:
        return render(request, 'staff.html')



def about_addNewImageCorousel(request):
    if request.method == 'POST':

        npos = request.POST['npos']
        uploaded_file = request.FILES.get('image')
        
        fs = FileSystemStorage(location='static/uploads/about')
        fs.save(uploaded_file.name, uploaded_file)
        corousel = AboutCorousel(image = uploaded_file.name,position = npos)
        corousel.save()

        messages.success(request, "New Image added Successfully to the Corousel")
        return redirect('staff')

    else:
        return render(request, 'staff.html')
    
def editOurPatron(request):

    if request.method == 'POST':

        ntext = request.POST['ntext']
        uploaded_file = request.FILES.get('image')
        patron = AboutLibrarian.objects.get(Sno = 1)

        if uploaded_file and ntext is not True:
            fs = FileSystemStorage(location='static/uploads/librarian')
            fs.save(uploaded_file.name, uploaded_file)

            patron.image = uploaded_file.name
            patron.text = ntext
            patron.save()

            messages.success(request, "New Image and content added Successfully to our patron")
            

        elif ntext is not True:
            fs = FileSystemStorage(location='static/uploads/librarian')
            fs.save(uploaded_file.name, uploaded_file)

            patron.image = uploaded_file.name
            patron.save()

            messages.success(request, "New Image  added Successfully to our patron")
        else:
            patron.text = ntext
            patron.save()
            messages.success(request, "New content added Successfully to our patron")

        return redirect('staff')
    
    else:
        return render(request, 'staff.html')


def editTheLibrarian(request):

    if request.method == 'POST':

        ntext = request.POST['ntext']
        uploaded_file = request.FILES.get('image')
        patron = AboutLibrarian.objects.get(Sno = 2)

        if uploaded_file != None and ntext:
            fs = FileSystemStorage(location='static/uploads/librarian')
            fs.save(uploaded_file.name, uploaded_file)

            patron.image = uploaded_file.name
            patron.text = ntext
            patron.save()

            messages.success(request, "New Image and content added Successfully to our The Librarian")
            

        elif ntext =="":
            fs = FileSystemStorage(location='static/uploads/librarian')
            fs.save(uploaded_file.name, uploaded_file)

            patron.image = uploaded_file.name
            patron.save()

            messages.success(request, "New Image  added Successfully to The Librarian")
        else:
            patron.text = ntext 
            patron.save()
            messages.success(request, "New content added Successfully to The Librarian")

        return redirect('staff')
    
    else:
        return render(request, 'staff.html')
    

def editNewArrivalBooks(request):
    if request.method == "POST":
        uploaded_file = request.FILES.get('image')
        lpos=request.POST['lpos']
        lastimage=request.POST['lastimage']
        npos=request.POST['npos']
        if uploaded_file is not None:
            # try:
            about = get_object_or_404(BooksNewArrival,position=lpos,image = lastimage)
            about.image=uploaded_file.name
            about.position=npos
            about.save()
            print("edited")
            fs = FileSystemStorage(location='static/uploads/books/new_arrival')
            fs.save(uploaded_file.name, uploaded_file)
            messages.success(request, "Selected Book Modified Successfully")
        # except:
            # print("exception occured")
            # messages.error(request, "There are multiples data found with same Image position please check that and try again")
            return redirect('staff')

        else:
            messages.error(request, "Invalid file type choosen, Please try again with correct file type")
        return redirect('staff')
    else:
        return render(request, 'staff.html')
    
def deleteNewArrivalBooks(request):
    if request.method == 'POST':

        image = request.POST['lastimage']
        book_pos = request.POST['book_pos']

        query = get_object_or_404(BooksNewArrival, position = book_pos, image = image).delete()
        messages.success(request, "Selected Image deleted Successfully from New Arrival")
        return redirect('staff')

    else:
        return render(request, 'staff.html')
    
def addImageNewArrivalBooks(request):
    if request.method == 'POST':

        npos = request.POST['npos']
        uploaded_file = request.FILES.get('image')
        
        corousel = BooksNewArrival(image = uploaded_file.name,position = npos)
        corousel.save()

        fs = FileSystemStorage(location='static/uploads/books/new_arrival')
        fs.save(uploaded_file.name, uploaded_file)
        messages.success(request, "New Image added Successfully to the Corousel")
        return redirect('staff')

    else:
        return render(request, 'staff.html')
    

def editTopPicksBooks(request):
    if request.method == "POST":
        uploaded_file = request.FILES.get('image')
        lpos=request.POST['lpos']
        lastimage=request.POST['lastimage']
        npos=request.POST['npos']
        if uploaded_file is not None:
            # try:
            about = get_object_or_404(BooksTopPicks,position=lpos,image = lastimage)
            about.image=uploaded_file.name
            about.position=npos
            about.save()
            print("edited")
            fs = FileSystemStorage(location='static/uploads/books/top_picks')
            fs.save(uploaded_file.name, uploaded_file)
            messages.success(request, "Selected Book Modified Successfully")
        # except:
            # print("exception occured")
            # messages.error(request, "There are multiples data found with same Image position please check that and try again")
            return redirect('staff')

        else:
            messages.error(request, "Invalid file type choosen, Please try again with correct file type")
        return redirect('staff')
    else:
        return render(request, 'staff.html')
 

     
def deleteTopPicksBooks(request):
    if request.method == 'POST':

        image = request.POST['lastimage']
        book_pos = request.POST['book_pos']

        query = get_object_or_404(BooksTopPicks, position = book_pos, image = image).delete()
        messages.success(request, "Selected Image deleted Successfully from New Arrival")
        return redirect('staff')

    else:
        return render(request, 'staff.html')
 


    
def addImageTopPicksBooks(request):
    if request.method == 'POST':

        npos = request.POST['npos']
        uploaded_file = request.FILES.get('image')
        
        corousel = BooksTopPicks(image = uploaded_file.name,position = npos)
        corousel.save()

        fs = FileSystemStorage(location='static/uploads/books/top_picks')
        fs.save(uploaded_file.name, uploaded_file)
        messages.success(request, "New Image added Successfully to the Corousel")
        return redirect('staff')

    else:
        return render(request, 'staff.html')
 