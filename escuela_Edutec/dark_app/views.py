from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def toggle_theme(request):
    current_theme = request.COOKIES.get('theme', 'light')
    new_theme = 'dark' if current_theme == 'light' else 'light'
    response = JsonResponse({'theme': new_theme})
    response.set_cookie('theme', new_theme)
    return response