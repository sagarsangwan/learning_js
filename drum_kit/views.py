from django.shortcuts import render

# Create your views here.


def home_page(request):
    pass
    return render(request, 'pages/drum-kit-home.html')
