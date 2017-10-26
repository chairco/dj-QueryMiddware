from django.conf.urls import url
from autosearch import views


urlpatterns = [
    url(r'^$', views.edc_glass_history),
    url(r'^cbv/$', views.EdcGlassHistoryList.as_view()),
    url(r'^viewset/$', views.EdcGlasscHistoryViewSet.as_view({'get': 'list'})),
]