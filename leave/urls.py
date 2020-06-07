from django.urls import path, include
from leave.views import Home
from rest_framework import routers
from leave import views

router = routers.DefaultRouter()
router.register(r'leavetype', views.LeaveTypeViewSet)
router.register(r'leave', views.LeaveViewSet)

urlpatterns = [
    path('leavetest/', Home, name='home'),
    path('api/', include(router.urls), ),
]
