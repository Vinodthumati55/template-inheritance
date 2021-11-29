from django.shortcuts import render

# Create your views here.
def boot1(request):
    return render(request,'parent.html')
def boot2(request):
    return render(request,'child.html')
