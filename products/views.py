from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

def HelloView(request):
    print(request.headers)
    return JsonResponse({"message": "Hello, world!"})

def HelloNameView(request, username):
    print(username)
    return JsonResponse({"message": f"Hello, {username}!"})
