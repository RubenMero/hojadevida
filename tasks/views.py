from django.shortcuts import render

def hoja_vida(request):
    return render(request, 'hoja_vida/cv.html')
