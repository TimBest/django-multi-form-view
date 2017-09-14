from django.core.urlresolvers import reverse

from multi_form_view import MultiFormView

from base.forms import ContactForm, UserForm


class ContactView(MultiFormView):
    form_classes = {
        'contact_form' : ContactForm,
        'user_form' : UserForm,
    }
    record_id = None
    template_name = 'contact.html'

    def get_success_url(self):
        return reverse('contact_sent')
