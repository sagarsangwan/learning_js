from django.shortcuts import render

# Create your views here.


def home_page(request):
    pass
    return render(request, 'drum_kit/index.html')
