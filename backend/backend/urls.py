from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import ItemViewSet

router = DefaultRouter()
router.register("items", ItemViewSet, basename="item")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]