from .views import get_faal,home
from django.urls import path , include

urlpatterns = [
    path('', home, name='home'),
    path('get-faal/', get_faal, name='get_faal'),
]