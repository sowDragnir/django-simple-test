# from rest_framework import routers
# from projects.api import ProjectViewSet

# router = routers.DefaultRouter()
# router.register('api/projects', ProjectViewSet, base_name='projects')
# urlpatterns = router.urls

from rest_framework import routers
from .api import ProjectViewSet

router = routers.DefaultRouter()

router.register('api/projects', ProjectViewSet, 'projects')
#router.register(r'projects', ProjectViewSet, base_name='projects')

urlpatterns = router.urls