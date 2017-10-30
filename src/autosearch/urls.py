from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers

from django.conf.urls import url

from autosearch import views


urlpatterns = [
    url(r'^edch/$', views.EdcGlassHistoryList.as_view()),
    url(r'^edcs/$', views.EdcSummaryList.as_view()),
    #url(r'^fbv/$', views.edc_glass_history),
    #url(r'^viewset/$', views.EdcGlasscHistoryViewSet.as_view({'get': 'list'})),
]

# Add suffix patterns
#urlpatterns = format_suffix_patterns(urlpatterns)

# Create a router and register our viewsets withit 
#router = routers.DefaultRouter()
#router.register(r'edcgh', views.EdcGlasscHistoryViewSet, base_name='edcgh')
#urlpatterns = router.urls
