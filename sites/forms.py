from django import forms
from .models import Project, Profile, Rating


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['username']
        widgets = {
        'category':forms.CheckboxSelectMultiple(),
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude=['user', 'project']


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        exclude=['overall_score','profile','project']
