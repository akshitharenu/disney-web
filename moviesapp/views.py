from django.shortcuts import render
from .models import customer,movie,Book
from django.contrib import messages
from django.http import JsonResponse
# Create your views here.
def index(request):
    return render(request,'index.html')
def register( request):
    if request.method=='POST':
        name=request.POST['name']
        phone = request.POST['phone']   
        email=request.POST['email']
        password=request.POST['password']

        emailExist = customer.objects.filter(email = email)
        phoneExist = customer.objects.filter(phone = phone)

        if(emailExist):
            messages.success(request,"E-mail Id already exist...!")
            return render(request,'register.html')
        elif(phoneExist):
            messages.success(request,"Phone number already exist...!")
            return render(request,'register.html')
        else:
            customer(name=name, phone = phone, email=email,password=password).save()
            messages.success(request,'The New customer '+request.POST['name']+" is saved Successfully...!")
            return render(request,'login.html')
    
    else:
        return render(request,'register.html') 
def login(request):
    if request.method=="POST":
       
        try:
            Userdetails=customer.objects.get(email=request.POST['email'],password=request.POST['password'])
            print("Username=",Userdetails)
            request.session['email']=Userdetails.email
            return render(request,'home.html')
        except customer.DoesNotExist as e:
            messages.success(request,'Username/Password Invalid...!')
    return render (request,'login.html') 
def home(request):
    
    return render(request,'home.html')
def moviepage(request):
    movielist=movie.objects.all()
    return render(request,'mov.html',{'movielist':movielist})
def moviedetail(request,movie_id):
    moviess=movie.objects.get(id=movie_id)
    return render(request,'moviedetail.html',{'moviess':moviess})

def books(request):
    bookss=Book.objects.all()
    return render(request,'books.html',{'bookss':bookss})
def bookdetail(request,book_id):
    booklist=Book.objects.get(id=book_id)
    return render(request,'bookdetail.html',{'booklist':booklist})
def movieapi(request):
    pt = movie.objects.values()
 
    if pt:

        return JsonResponse({
            'error' : False,
            'message' : 'movies retrieved successfully',
            'data':list(pt)
            })
    else:
        return JsonResponse({
            'error' : True,
            'message' : 'movies not found'
 
            })
# def singlemovieapi(request,movie_id):
#     vv=movie.objects.get(id=movie_id)
#     if vv:
#          return JsonResponse({
#             'error' : False,
#             'message' : 'movies retrieved successfully',
#             'data':list(vv)
#             })
#     else:
#         return JsonResponse({
#             'error' : True,
#             'message' : 'movies not found'
 
#             })
