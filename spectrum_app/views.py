from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
import smtplib, ssl
def home(request):
    all_photos = AllPhoto.objects.all()
    slider = SliderPhoto.objects.all()
    showcase_photos = WeddingCouple.objects.all().order_by('-id')
    i=0
    photos =[]
    for photo in showcase_photos:
        if i <3:
            photos.append(photo)
            i +=1
        else:
            break 
    context = {
        'photos':photos,
        'slider':slider,
        'all_photos':all_photos,
    }
    return render(request,'spectrum_app/main.html',context)

def about(request):
    return render(request,'spectrum_app/about.html')

def gallery(request):
    photos = WeddingCouple.objects.all()
    return render(request,'spectrum_app/gallery.html',{'photos':photos})




def PhotoShow(request,name):
    couple = WeddingCouple.objects.get(name=name)
    photos = WeddingPhoto.objects.filter(couple=couple).order_by('id')
    images = []
    context = {
        'couple':couple,
        'photos':photos,
    }
    return render(request,'spectrum_app/photo_show.html',context)

def Booking(request):
    if request.method == "POST":
        name = request.POST.get("name")    
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        date = request.POST.get("date")
        shoot_type = request.POST.get("shoot_type")
        place = request.POST.get("place")
        book = Book(name=name,email=email,mobile=mobile,date=date,shoot_type=shoot_type,place=place)
        book.save()
        # port = 465 
        # smtp_server = "smtp.gmail.com"
        # sender_email = "" 
        # receiver_email = ""  
        # password = ""
        # SUBJECT = "Spectrum Studio Booking"   
        # TEXT = name+" "+mobile+" "+shoot_type+" "+date+" "+place
        # message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
        # context = ssl.create_default_context()
        # with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        #     server.login(sender_email, password)
        #     server.sendmail(sender_email, receiver_email, message)
        messages.success(request,'Successfully booked')
        return redirect("/")
    else:
      return render(request,'spectrum_app/realbook.html')

def Show_by_type(request,type):
    main = AllPhoto.objects.filter(photo_type=type)
    
    photos =[]
    for m in main:
        photo = Photo.objects.filter(main=m)
        for p in photo:
            photos.append(p.img)
    context = {'photos':photos}
    return render(request,'spectrum_app/showbytype.html',context)

def photographer(request,name):
    main = AllPhoto.objects.filter(c_man=name)
    photos =[]
    for m in main:
        photo = Photo.objects.filter(main=m)
        for p in photo:
            photos.append(p.img)
    context = {'photos':photos}
    return render(request,'spectrum_app/showbytype.html',context)

def films(request):
    return render(request,'spectrum_app/films.html')

def map(request):
    return render(request,'spectrum_app/map.html')