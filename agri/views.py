from django.shortcuts import render

from django.http import HttpResponse


from joblib import load

model=load("mysite/scrop.joblib")

def home(request):
    return render(request,"home.html")


def predict(request):
    n=request.POST.get("n")
    p=request.POST.get("p")
    k=request.POST.get("k")
    temp=request.POST.get("temp")
    humd=request.POST.get("humd")
    phl=request.POST.get("phl")
    rain=request.POST.get("rain")
    inp=[[n,p,k,temp,humd,phl,rain]]
   # yp=model.predict(inp)
    return render(request,"predict.html")

