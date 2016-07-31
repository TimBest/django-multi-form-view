from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from base import views


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^records/$', views.RecordListView.as_view(), name='records'),
    url(r'^records/new/$', views.RecordFormView.as_view(), name='records_new'),
    url(r'^records/edit/(?P<record_id>\d+)$', views.RecordFormView.as_view(), name='records_edit'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
