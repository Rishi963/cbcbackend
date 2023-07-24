
from backend import views

from django.urls import include, path
from rest_framework import routers
from .views import RegisterAPI

router = routers.DefaultRouter()

router.register(r'data', views.DataView)
router.register(r'studentreg', views.StudentregView)
router.register(r'course', views.CourseView)
router.register(r'branch', views.BranchView)
router.register(r'reference', views.ReferenceView)
router.register(r'billing', views.BillingView)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]
