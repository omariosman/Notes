from django.conf.urls import url
from . import views


app_name = 'notes_app'

urlpatterns = [
    url(r'^$', views.all_notes, name='all_notes'),
    url(r'^(?P<slug>[-\w]+)$', views.note_details, name='note_details'),
    url(r'^add$', views.note_add, name='note_add'),

]