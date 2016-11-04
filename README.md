# Django Multi. Form View
[![CircleCI](https://circleci.com/gh/TimBest/django-multi-form-view.svg?style=shield)](https://circleci.com/gh/TimBest/django-multi-form-view)
[![codecov](https://codecov.io/gh/timbest/django-multi-form-view/branch/master/graph/badge.svg)](https://codecov.io/gh/timbest/django-multi-form-view)
[![PyPI](https://img.shields.io/pypi/v/django-multi-form-view.svg?maxAge=2592000)](https://pypi.python.org/pypi/django-multi-form-view)
[![PyPI](https://img.shields.io/pypi/dm/django-multi-form-view.svg?maxAge=2592000)](https://pypi.python.org/pypi/django-multi-form-view)

Django class based views for using more than one Form or ModelForm in a single view.

## Install
```bash
$ pip install django-multi-form-view
```

## Example
```python
from multi_form_view import MultiModelFormView

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
```

## Demo
```bash
$ cd demo
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py runserver
```

## Testing
```bash
$ python demo/manage.py behave
```
