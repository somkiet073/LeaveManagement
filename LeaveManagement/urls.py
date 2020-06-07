from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls


API_TITLE = 'Leave Management API'
API_DESCRIPTION = 'A Web API for creating'
schema_view = get_schema_view(title=API_TITLE)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('employee/', include('employee.urls',)),
    path('leave/', include('leave.urls',)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('schema/', schema_view),
    path('docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),
]
