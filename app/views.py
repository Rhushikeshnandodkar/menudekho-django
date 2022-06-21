from xml.etree.ElementTree import QName
from django.shortcuts import redirect, render
from .models import Mess
import os
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db.models import Q
# Create your views here.
def index(request):
    veg_mess_object = Mess.objects.filter(is_veg=True)
    non_veg_mess_object = Mess.objects.filter(is_veg=False)
    all_mess_object = Mess.objects.all()
    context = {'mess':veg_mess_object, 'all_mess':all_mess_object, 'non_veg':non_veg_mess_object}
    return render(request, "home.html", context)

def update(request, pk):
    mess_object = Mess.objects.get(mess_id=pk)
    if mess_object.user == request.user:
        if request.method == "POST":
            if len(request.FILES) != 0:
                if len(mess_object.image) > 0:
                    os.remove(mess_object.image.path)
                mess_object.image = request.FILES['image']
            mess_object.title = request.POST.get('title')
            mess_object.desc = request.POST.get('desc')
            mess_object.price = request.POST.get('price')
            mess_object.address = request.POST.get('address')
            mess_object.dish1 = request.POST.get('dish1')
            mess_object.dish2 = request.POST.get('dish2')
            mess_object.dish3 = request.POST.get('dish3')
            mess_object.dish4 = request.POST.get('dish4')
            mess_object.dish5 = request.POST.get('dish5')
            mess_object.dish6 = request.POST.get('dish6')
            mess_object.dish7 = request.POST.get('dish7')
            mess_object.owner = request.POST.get('owner')
            mess_object.contact_owener = request.POST.get('contact_owner')
            mess_object.is_veg = bool(request.POST.get('enable'))
            mess_object.save()
            return redirect('/')
    else:
        return redirect('profile')
   
    context = {'mess':mess_object}
    return render(request, "updatemess.html", context)

def handlelogin(request):
    if request.method == "POST":
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return redirect('/')
    return render(request, "login.html")

def profile(request):
    if Mess.objects.filter(user=request.user).exists():
        user_mess = Mess.objects.get(user=request.user)
        context = {'mess':user_mess}
    else:
        print('hello')
        return redirect('/')
    return render(request, "profile.html", context)

def detail(request, pk):
    detail_mess = Mess.objects.get(mess_id=pk)
    context = {'detail_mess':detail_mess}
    return render(request, "detail.html", context)

def search(request):
    query = request.GET['query']
    producttitle = Mess.objects.filter(Q(title__icontains=query) | Q(desc__icontains=query) | Q(dish1__icontains=query) | Q(dish2__icontains=query) | Q(dish7__icontains=query) | Q(dish6__icontains=query) | Q(dish5__icontains=query) | Q(dish4__icontains=query) | Q(dish3__icontains=query))
    # holderaddress = Mess.objects.filter(address__icontains=query)
    # finalprod = producttitle.union(holderaddress)
    return render(request, "search.html", {'mess':producttitle})
