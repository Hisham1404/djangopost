from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request,'base.html')

def details(request):
    val1 = request.POST['text']
    val2 = request.POST['email']
    res = val1 , val2

    return render(request, 'submit.html',{'result': res})
