from django.contrib import admin
from .models import CustomUser, Course, CourseMaterial, Enrollment, Feedback, Status

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor')
    search_fields = ('title', 'instructor__username')

class CourseMaterialAdmin(admin.ModelAdmin):
    list_display = ('name', 'course')
    search_fields = ('name', 'course__title')

class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'date_enrolled')
    list_filter = ('course', 'date_enrolled')

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('course', 'student', 'created_at')
    list_filter = ('course', 'created_at')

class StatusAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at')
    search_fields = ('user__username', 'text')


# Registering the models with the admin site
admin.site.register(CustomUser)
admin.site.register(Course, CourseAdmin)
admin.site.register(CourseMaterial, CourseMaterialAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Status, StatusAdmin)