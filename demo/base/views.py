from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.views.generic.list import ListView

from multi_form_view import MultiModelFormView

from base.forms import PhotoForm, RecordForm
from base.models import Photo, Record


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

    def get_objects(self):
        self.record_id = self.kwargs.get('record_id', None)
        try:
            record = Record.objects.get(id=self.record_id)
        except Record.DoesNotExist:
            record = None
        return {
          'record_form': record,
          'photo_form': record.photo if record else None
        }

    def get_success_url(self):
        return reverse('records')

    def forms_valid(self, forms):
        photo = forms['photo_form'].save()
        record = forms['record_form'].save(commit=False)
        record.photo = photo
        record.save()
        return HttpResponseRedirect(self.get_success_url())
