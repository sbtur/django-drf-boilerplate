from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r"example", views.ExampleView, basename="example")

urlpatterns = router.urls
