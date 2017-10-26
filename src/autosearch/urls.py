from django.conf.urls import url
from autosearch import views


urlpatterns = [
    url(r'^$', views.edc_glass_history),
    #url(r'^(?P<glassid>.+)/$', views.edc_glass_history),
]