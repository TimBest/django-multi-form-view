from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from base import views


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),

    url(r'^records/$', views.RecordListView.as_view(), name='records'),
    url(r'^records/new/$', views.RecordFormView.as_view(), name='records_new'),
    url(r'^records/edit/(?P<record_id>\d+)$', views.RecordFormView.as_view(), name='records_edit'),

    url(r'^contact/$', views.ContactView.as_view(), name='contact'),
    url(r'^cntact/sent/$', TemplateView.as_view(template_name='contact-sent.html'), name='contact_sent'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
