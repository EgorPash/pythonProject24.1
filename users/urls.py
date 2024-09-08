from rest_framework.routers import DefaultRouter
from users.apps import UsersConfig

app_name = UsersConfig.name

router = DefaultRouter()
# router.register(r'users', CourseViewSet, basename='courses')

urlpatterns = [

] + router.urls