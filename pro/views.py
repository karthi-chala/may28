from django.shortcuts import render

def sample(request):
    return render(request,'home.html')

def sample1(request):
    return render(request,'movies.html')

def sample2(request):
    return render(request,'tvshows.html')