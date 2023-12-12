from django.shortcuts import render
from translate import Translator
import requests
from .models import Faal
import random

def home(request):
    return render(request, 'home.html')
    

# Create your views here.
def get_faal(request):
    
    # Falls = Faal.objects.all()
    # for fal in Falls :
    #     url = f'https://api.ganjoor.net/api/ganjoor/poem/{2129+fal.id}/recitations'
    #     response = requests.get(url)
    #     if response.status_code == 200:
    #         data = response.json()
    #         if data:
    #             fal.mp3_url = data[0]["mp3Url"]
    #             fal.save()
        
    
    
    random_number = random.randint(1, 495)
    faal_object = Faal.objects.get(id=random_number)
    return render(request, 'faal/faal_detail.html', {'faal': faal_object})