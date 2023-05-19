from django.shortcuts import render

def necklaces(request):
    return render(request,'section/necklaces.html')
# Create your views here.
def rings(request):
    return render(request,'section/rings.html')

def earrings(request):
    return render(request,'section/earrings.html')