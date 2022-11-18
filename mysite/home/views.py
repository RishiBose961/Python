from django.shortcuts import render,HttpResponse
from home.models import Contact
# Create your views here.
def index(request):
    context={
        "variable": "this is sent...."
    }
    return render(request,'index.html',context)

def about(request):
    return HttpResponse("hello kaya hal ha:.....")
    #return render(request,'about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        contact = Contact(name=name,email=email,phone=phone)
        contact.save()
    return render(request,'contact.html')

