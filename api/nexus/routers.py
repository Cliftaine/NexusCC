from .views import TeamsViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'teams',TeamsViewSet,basename = 'teams')

urlpatterns = router.urls
