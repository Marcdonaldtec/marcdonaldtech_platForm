# MainApp/views.py
from django.shortcuts import render
from UserApp.models import UserProfile

def home(request):
    # Récupérez tous les utilisateurs par ordre chronologique du plus récent
    users = UserProfile.objects.all().order_by('-user__date_joined')
    return render(request, 'MainApp/home.html', {'users': users})
