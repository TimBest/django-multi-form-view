from django import forms

from base.models import Photo, Profile, Record


class PhotoForm(forms.ModelForm):

    class Meta(object):
        model = Photo
        fields = ['image', 'tag']


class RecordForm(forms.ModelForm):

    class Meta(object):
        model = Record
        fields = ['title', 'description']

class ProfileForm(forms.ModelForm):

    class Meta(object):
        model = Profile
        fields = ['name']


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)


class UserForm(forms.Form):
    sender_email = forms.EmailField()
