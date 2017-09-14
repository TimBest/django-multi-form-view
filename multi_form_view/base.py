"""
Django class based views for using more than one Form or ModelForm in a single view.
"""
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import FormView
import six


class MultiFormView(FormView):
    """
    View to handle multiple form classes.
    """
    form_classes = {}

    def are_forms_valid(self, forms):
        """
        Check if all forms defined in `form_classes` are valid.
        """
        for form in six.itervalues(forms):
            if not form.is_valid():
                return False
        return True

    def forms_valid(self, forms): #pylint: disable=unused-argument
        """
        Redirects to get_success_url().
        """
        return HttpResponseRedirect(self.get_success_url())

    def forms_invalid(self, forms):
        """
        Renders a response containing the form errors.
        """
        context = self.get_context_data(forms=forms)
        return render(self.request, self.template_name, context)

    def get(self, request, **kwargs):
        """
        Render the forms.
        """
        context = self.get_context_data()
        return render(request, self.template_name, context=context)

    def get_context_data(self, **kwargs):
        """
        Add forms into the context dictionary.
        """
        context = {}
        if 'forms' not in kwargs:
            context['forms'] = self.get_forms()
        else:
            context['forms'] = kwargs['forms']
        return context

    def get_forms(self):
        """
        Initializes the forms defined in `form_classes` with initial data from `get_initial()` and
        kwargs from get_form_kwargs().
        """
        forms = {}
        initial = self.get_initial()
        form_kwargs = self.get_form_kwargs()
        for key, form_class in six.iteritems(self.form_classes):
            forms[key] = form_class(initial=initial[key], **form_kwargs[key])
        return forms

    def get_form_kwargs(self):
        """
        Build the keyword arguments required to instantiate the form.
        """

        kwargs = {}
        for key in six.iterkeys(self.form_classes):
            if self.request.method in ('POST', 'PUT'):
                kwargs[key] = {
                    'data': self.request.POST,
                    'files': self.request.FILES,
                }
            else:
                kwargs[key] = {}
        return kwargs

    def get_initial(self):
        """
        Returns a copy of `initial` with empty initial data dictionaries for each form.
        """
        initial = super(MultiFormView, self).get_initial()
        for key in six.iterkeys(self.form_classes):
            initial[key] = {}
        return initial

    def post(self, request, **kwargs):
        """
        Uses `are_forms_valid()` to call either `forms_valid()` or * `forms_invalid()`.
        """
        forms = self.get_forms()
        if self.are_forms_valid(forms):
            return self.forms_valid(forms)
        else:
            return self.forms_invalid(forms)


class MultiModelFormView(MultiFormView):
    """
    View to handle multiple model form classes.
    """

    def forms_valid(self, forms):
        """
        Calls `save()` on each form.
        """
        for form in six.itervalues(forms):
            form.save()
        return super(MultiModelFormView, self).forms_valid(forms)

    def get_forms(self):
        """
        Initializes the forms defined in `form_classes` with initial data from `get_initial()`,
        kwargs from get_form_kwargs() and form instance object from `get_objects()`.
        """
        forms = {}
        objects = self.get_objects()
        initial = self.get_initial()
        form_kwargs = self.get_form_kwargs()
        for key, form_class in six.iteritems(self.form_classes):
            forms[key] = form_class(instance=objects[key], initial=initial[key], **form_kwargs[key])
        return forms

    def get_objects(self):
        """
        Returns dictionary with the instance objects for each form. Keys should match the
        corresponding form.
        """
        objects = {}
        for key in six.iterkeys(self.form_classes):
            objects[key] = None
        return objects
