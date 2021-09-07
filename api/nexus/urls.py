from django.urls import path, include
from .views import UserView, LoginView, LogoutView, TeamViewSet, MovementsListCreateView, MovementsRetrieveView, MovementsViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'teams',TeamViewSet,basename = 'teams')
router.register(r'accounts',TeamViewSet,basename = 'accounts')
router.register(r'movements', MovementsViewSet, basename= 'movements')
router.register(r'users', UserView, basename= 'Users')

urlpatterns = [
        path('login/', LoginView.as_view()),
        path('logout/', LogoutView.as_view())
]

urlpatterns+=router.urls
