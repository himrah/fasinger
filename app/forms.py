from app.models import *
from django.forms import *
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import authenticate
from PIL import Image
from django import forms
class ImageInputForm(forms.ModelForm):
    class Meta:
        model = Photos
        fields = ('original_photo',)


class PhotoForm(forms.ModelForm):
    #x = forms.FloatField(widget=forms.HiddenInput())
    #y = forms.FloatField(widget=forms.HiddenInput())
    #width = forms.FloatField(widget=forms.HiddenInput())
    #height = forms.FloatField(widget=forms.HiddenInput())

    class Meta:
        model = Photos
        fields = ('original_photo',)
        
        
        #fields = ('photo', 'x', 'y', 'width', 'height', )
    """def save(self):
        Photo = super(PhotoForm, self).save()

        x = self.cleaned_data.get('x')
        y = self.cleaned_data.get('y')
        w = self.cleaned_data.get('width')
        h = self.cleaned_data.get('height')

        image = Image.open(Photo.photo)
        cropped_image = image.crop((x, y, w+x, h+y))
        resized_image = cropped_image.resize((200, 200), Image.ANTIALIAS)
        resized_image.save(Photo.photo.path)
        return Photo"""


class Comment_form(forms.ModelForm):
    comment = forms.CharField(label="Username", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Comment here...'}))
    class Meta:
        model = Comments
        fields = ('comment',)


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username','placeholder':'Username'}))
    password = forms.CharField(label="Password", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password','type':'password','placeholder':'Password'}))

    def clean(self,*args,**kwargs):
        username =self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username,password=password)
            if not user:
                raise forms.ValidationError("this user doest not exist")
        return super(LoginForm,self).clean(*args,**kwargs)        