from django.core.urlresolvers import reverse
from django.views.generic.list import ListView

from multi_form_view import MultiModelFormView

from base.forms import PhotoForm, ProfileForm
from base.models import Photo, Profile


class ProfileListView(ListView):
    template_name = 'profiles.html'
    model = Profile


class ProfileFormView(MultiModelFormView):
    form_classes = {
        'avatar_form' : PhotoForm,
        'background_form' : PhotoForm,
        'profile_form' : ProfileForm,
    }
    record_id = None
    template_name = 'profiles_form.html'

    def get_form_kwargs(self):
        kwargs = super(ProfileFormView, self).get_form_kwargs()
        kwargs['avatar_form']['prefix'] = 'avatar'
        kwargs['background_form']['prefix'] = 'background'
        return kwargs

    def get_objects(self):
        self.profile_id = self.kwargs.get('profile_id', None)
        try:
            profile = Profile.objects.get(id=self.profile_id)
        except Profile.DoesNotExist:
            profile = None
        return {
            'profile_form': profile,
            'avatar_form': profile.avatar if profile else None,
            'background_form': profile.background if profile else None,
        }

    def get_success_url(self):
        return reverse('profiles')

    def forms_valid(self, forms):
        profile = forms['profile_form'].save(commit=False)
        profile.avatar = forms['avatar_form'].save()
        profile.background = forms['background_form'].save()
        profile.save()
        return super(ProfileFormView, self).forms_valid(forms)
