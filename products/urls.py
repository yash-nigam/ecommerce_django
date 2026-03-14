from django.urls import path
from products import views

urlpatterns = [
    path('hello/', views.HelloView, name='hello'),
    path('hello/<slug:username>', views.HelloNameView, name='hello_name'),
]
