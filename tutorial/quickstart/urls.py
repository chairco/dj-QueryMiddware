from django.conf.urls import url
from quickstart import views


urlpatterns = [
    url(r'^quickstart/(?P<pk>[0-9]+)/$', views.edc_glass_history),
]
