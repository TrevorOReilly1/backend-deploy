"""
URLs for the Skills API
Allows list, create, update, and delete of skills
"""

from django.contrib import admin
from django.urls import path, re_path
from django.views.static import serve
from django.conf import settings
from api import views

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Static & media (PythonAnywhere deployment)
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),

    # API endpoints (clean REST structure)
    path('api/skills/', views.skillsListCreate.as_view(), name='skills-list-create'),
    path('api/skills/<int:pk>/', views.skillRetrieveUpdateDestroy.as_view(), name='skills-detail'),
]
