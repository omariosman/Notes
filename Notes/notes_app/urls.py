from django.conf.urls import url
from . import views


app_name = 'notes_app'

urlpatterns = [
    url(r'^$', views.all_notes, name='all_notes'),
    url(r'^add$', views.note_add, name='note_add'),
    url(r'^(?P<slug>[-\w]+)$', views.note_details, name='note_details'),
    url(r'^(?P<slug>[-\w]+)/edit$', views.note_edit, name='note_edit'),
]
