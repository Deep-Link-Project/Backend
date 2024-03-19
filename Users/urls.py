from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register('member',views.MemberView,basename='member')

urlpatterns = router.urls
