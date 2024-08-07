from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request, 'test_app/home_page.html')

def display_map(request):
    return render(request, 'test_app/map_page.html')


