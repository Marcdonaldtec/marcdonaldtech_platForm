# ProjectApp/forms.py
from django import forms
from .models import Project
from CategoryApp.models import Category

class ProjectForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Project
        fields = ['title', 'description', 'photo', 'categories']  # Ajoutez les champs nécessaires
