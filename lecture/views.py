from django.shortcuts import render

def angular(request):
    return render(request, "angular.html")

def presentation(request):
    return render(request, "presentation.html")