from django.conf.urls import url
from quickstart import views


urlpatterns = [
    url(r'^(?P<glass_id>\w+)/$', views.edc_glass_history),
]
