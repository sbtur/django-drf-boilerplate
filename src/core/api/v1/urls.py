from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r"example", views.ExampleView, base_name="example")

urlpatterns = router.urls
