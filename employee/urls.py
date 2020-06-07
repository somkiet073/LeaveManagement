from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers
from employee import views
from django.conf import settings
from django.views.static import serve

router = routers.DefaultRouter()
router.register(r'employee', views.UserViewSet)
router.register(r'group', views.GroupViewSet)
router.register(r'AppoveGroup', views.AppoveGroupViewSet)
router.register(r'Department', views.DepartmentViewSet)
router.register(r'Positions', views.PositionsViewSet)
router.register(r'Prename', views.PrenameViewSet)
router.register(r'Profile', views.ProfileViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT, 
        }),
    ]
