from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from django.conf.urls import handler404

# Initialize the default router
router = DefaultRouter()

# Register the CustomUserViewSet with the router
router.register(r'users', views.CustomUserViewSet, basename='users')

urlpatterns = [
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('courses/', views.courses, name='courses'),
    path('home', views.home_redirect, name='home_redirect'),
    path('home/<str:username>/', views.home, name='home'),
    path('delete_status/<int:status_id>/', views.delete_status, name='delete_status'),
    path('courses/<int:course_id>/', views.course_detail, name='course_detail'),
    path('courses/<int:course_id>/enroll/', views.enroll_in_course, name='enroll_in_course'),
    path('courses/<int:course_id>/unenroll/', views.unenroll_from_course, name='unenroll_from_course'),
    path('course/delete/<int:course_id>/', views.delete_course, name='delete_course'),
    path('courses/<int:course_id>/feedback/', views.leave_feedback, name='leave_feedback'),
    path('materials/delete/<int:material_id>/', views.delete_material, name='delete_material'),
    path('delete_feedback/<int:feedback_id>/', views.delete_feedback, name='delete_feedback'),
    path('chat/<str:room_name>/', views.room, name='room'),
    path('search/', views.user_search, name='user_search'),
    path('', views.user_login, name='login'),

    # Api Path
    path('api/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
