from django.shortcuts import render
from .models import Person

def home(request):
    if False:
        persion=Person()
        persion.first_name = 'aravind'
        persion.last_name = 'ponnala'
        persion.save()
    return render(request, 'index.html')