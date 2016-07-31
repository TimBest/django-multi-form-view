from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.views.generic.list import ListView

from multi_form_view import MultiModelFormView

from base.forms import PhotoForm, RecordForm
from base.models import Record, Photo


class IndexView(TemplateView):
    template_name = "base.html"


class RecordListView(ListView):
    template_name = 'records.html'
    model = Record


class RecordFormView(MultiModelFormView):
    form_classes = {
      'photo_form' : PhotoForm,
      'record_form' : RecordForm
    }
    record_id=None
    template_name = 'records_form.html'
    success_url = '/records/' # reverse('records')

    def get_objects(self, queryset=None):
        self.record_id = self.kwargs.get('record_id', None)
        try:
            record = Record.objects.get(id=self.record_id)
        except Record.DoesNotExist:
            record = None
        return {
          'record_form': record,
          'photo_form': record.photo if record else None
        }

    def forms_valid(self, forms):
        photo = forms['photo_form'].save()
        record = forms['record_form'].save(commit=False)
        record.photo = photo
        record.save()
        return HttpResponseRedirect(self.get_success_url())

    # def forms_valid(self, forms):
    #     # album = forms['albumForm'].save(request=self.request, commit=False)
    #     # if self.request.FILES.get('image'):
    #     #     album.album_art = Image.objects.create(
    #     #         image=self.request.FILES.get('image'),
    #     #         title = album.title,
    #     #         user = self.request.user
    #     #     )
    #     # elif self.request.POST.get('album_art'):
    #     #     imageId = self.request.POST.get('album_art')
    #     #     album.album_art = get_object_or_None(Image, id=imageId)
    #     # album.save()
    #     # forms['albumForm'].save(request=self.request)
    #     # forms['albumForm'].save_m2m()
    #     return HttpResponseRedirect(self.get_success_url())
