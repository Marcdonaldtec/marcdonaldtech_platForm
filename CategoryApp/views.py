from django.shortcuts import render
from .models import Category

app_name = 'CategoryApp'
def all_categories(request):
    categories = Category.objects.all()
    return render(request, 'CategoryApp/all_categories.html', {'categories': categories})
