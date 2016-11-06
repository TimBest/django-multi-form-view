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

## Usage

### MultiFormView ([Example](demo/base/views.py))
**class multi_form_view.MultiFormView**  
A single view that can display multiple Django forms. Handles displaying, redisplaying on error, and
redirects on form success in.

#### Extends
* django.views.generic import FormView

#### Attributes and Methods
* `form_classes`  
  A dictionary containing to forms for the view.
* `are_forms_valid()`  
  Check if all forms defined in `form_classes` are valid.
* `forms_valid()`  
  Redirects to get_success_url().
* `forms_invalid()`  
  Renders a response containing the form errors.
* `get()`  
  Render the forms.
* `get_context_data()`  
  Adds the results of `get_forms()` to the context dictionary with the key `'forms'`.
* `get_forms()`.  
  Initializes the forms defined in `form_classes` with initial data from `get_initial()` and kwargs
  from get_form_kwargs().
* `get_form_kwargs()`.
  Build the keyword arguments required to instantiate the form.  
* `get_initial()`  
  Returns a copy of `initial` with empty initial data dictionaries for each form.
* `post()`
  Uses `are_forms_valid()` to call either `forms_valid()` or `forms_invalid()`.

### MultiModelFormView ([Example](demo/base/views.py))
**class multi_form_view.MultiModelFormView**  
A single view that can display multiple Django ModelForms. Handles displaying, redisplaying on
error, and redirects on form success in.

#### Extends
* multi_form_view.MultiFormView

#### Attributes and Methods
* `forms_valid()`  
  Calls `save()` on each form.
* `get_forms()`.  
  Initializes the forms defined in `form_classes` with initial data from `get_initial()`, kwargs
  from get_form_kwargs() and form instance object from `get_objects()`.
* `get_objects()`  
  Returns dictionary with the instance objects for each form. Keys should match the corresponding
  form.

## Demo
```bash
$ cd demo
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py runserver
```

## Testing
Install [PhantomJS](http://phantomjs.org/)
```bash
$ python demo/manage.py behave
```
