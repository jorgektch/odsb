from rest_framework import routers, serializers, viewsets
from .views import *
from .models import *
from .api import *

router = routers.DefaultRouter()

router.register('api/institution', InstitutionViewSet, 'institution' )
router.register('api/ods', OdsViewSet, 'ods')
router.register('api/information_sources', InformationSourcesViewSet, 'information_sources')

urlpatterns = router.urls
