from django.shortcuts import render,HttpResponse

# Create your views here.
tload=0
def index(request):
    global tload
    tload=tload+1
    context ={
        'tload':tload
    }
    return render(request,'index.html',context)


def saveform(request):
    if request.method=="POST":
        name =request.POST.get('name')
        mobile =request.POST.get('mobile')
        print(name,mobile)
    return HttpResponse("ajax runnung...")
