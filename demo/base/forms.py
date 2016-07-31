from django import forms

from base.models import Photo, Record


class PhotoForm(forms.ModelForm):

    class Meta(object):
        model = Photo
        fields = ['image', 'tag']


class RecordForm(forms.ModelForm):

    class Meta(object):
        model = Record
        fields = ['title', 'description']
