from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import FormView


class MultiFormView(FormView):
    """ Mixin to handle multiple form classses """
    form_classes = {}
    template_name = None
    success_url = '/'

    def are_forms_valid(self, forms):
        for form in forms.itervalues():
            if not form.is_valid():
                return False
        return True

    def forms_valid(self, forms):
        for form in forms.itervalues():
            form.save()
        return HttpResponseRedirect(self.get_success_url())

    def forms_invalid(self, forms):
        context = self.get_context_data()
        context.update(forms)
        return render(self.request, self.template_name, context)

    def get_context_data(self, **kwargs):
        if 'view' not in kwargs:
            kwargs['view'] = self
        return kwargs

    def get(self, request, **kwargs):
        context = self.get_context_data()
        context.update(self.get_forms())
        return render(request, self.template_name, context=context)

    def get_forms(self):
        forms = {}
        initial = self.get_initial_data()
        form_kwargs = self.get_form_kwargs()
        for key, form_class in self.form_classes.iteritems():
            forms[key] = form_class(initial=initial[key], **form_kwargs)
        return forms

    def get_form_kwargs(self):
        kwargs = {}
        if self.request.method in ('POST', 'PUT'):
            kwargs.update({
                'data': self.request.POST,
                'files': self.request.FILES,
            })
        return kwargs

    def get_initial_data(self):
        initial = {}
        for key in self.form_classes.iterkeys():
            initial[key] = {}
        return initial

    def post(self, request, **kwargs):
        forms = self.get_forms()
        if self.are_forms_valid(forms):
            return self.forms_valid(forms)
        else:
            return self.forms_invalid(forms)


class MultiModelFormView(MultiFormView):
    """ The object coresponding to the form must use the sam key """

    def get_objects(self):
        objects = {}
        for key in self.form_classes.iterkeys():
            objects[key] = None
        return objects

    def get_forms(self):
        forms = {}
        objects = self.get_objects()
        initial = self.get_initial_data()
        form_kwargs = self.get_form_kwargs()
        for key, form_class in self.form_classes.iteritems():
            forms[key] = form_class(instance=objects[key], initial=initial[key], **form_kwargs)
        return forms
