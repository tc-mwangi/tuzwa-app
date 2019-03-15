from django import forms
from sites.models import Project, Profile


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
        ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs = {
            'class': 'form-control'
        }
        ))


class ProjectForm(forms.Form):
    '''creates instance of the form for posting projects
    
    Arguments:
        forms {[type]} -- [description]
    '''

    class Meta:
        model = Project
        exclude = ['editor', 'pub_date']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }



class ProfileForm(forms.Form):
    '''creates instance of the form for posting profile information
    
    Arguments:
        forms {[type]} -- [description]
    '''





class RatingForm(forms.Form):
    '''creates instance of the form for posting ratings on projects
    
    Arguments:
        forms {[type]} -- [description]
    '''


class ProjectForm(forms.ModelForm):
    class Meta:
        model=Project
        exclude=['username','post_date','design','usability','creativity','content','overall_score','avatar','country']
        widgets={
        'colors':forms.CheckboxSelectMultiple(),
        'technologies':forms.CheckboxSelectMultiple(),
        'categories':forms.CheckboxSelectMultiple(),
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['username']

class RatingForm(forms.ModelForm):
    class Meta:
        model=Rating
        exclude=['overall_score','profile','project']


