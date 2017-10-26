from django.conf.urls import url
from quickstart import views


urlpatterns = [
    url(r'^$', views.edc_glass_history),
]
