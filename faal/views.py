from django.shortcuts import render
from translate import Translator
import requests

def home(request):
    
    return render(request, 'home.html')
    

# Create your views here.
def get_faal(request):
    api_url = 'https://api.ganjoor.net/api/ganjoor/hafez/faal'
    response = requests.get(api_url)
    faal_data = response.json()
    translator= Translator(to_lang="it")
    translation = translator.translate(faal_data['plainText'][:500])
    faal_object = {
        'title': faal_data['title'],
        'full_title': faal_data['fullTitle'],
        'html_text': faal_data['plainText'].replace('\r\n','<br/>') + translation,
        'mp3_url': faal_data['recitations'][0]['mp3Url'],  # Assuming you want the first recitation
    }

    return render(request, 'faal/faal_detail.html', {'faal': faal_object})