from django.urls import include, path
from rest_framework.routers import DefaultRouter
from quickstart import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-login-logout/', include('rest_framework.urls', namespace='rest_framework'))
]



