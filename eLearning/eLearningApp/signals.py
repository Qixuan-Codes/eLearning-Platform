from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Enrollment, CourseMaterial
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

# Notify teacher if a student enrolls in the course
@receiver(post_save, sender=Enrollment)
def notify_teacher_on_enrollment(sender, instance, created, **kwargs):
    if created:
        message = f"{instance.student.full_name} has enrolled in your course: {instance.course.title}."
        group_name = f'notifications_{instance.course.instructor.username}'

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            group_name,
            {
                'type': 'user_notification',
                'notification_type': 'enrollment',
                'message': message
            }
        )

# Notify student if there is a new course material
@receiver(post_save, sender=CourseMaterial)
def notify_students_on_new_material(sender, instance, created, **kwargs):
    if created:
        enrolled_students = instance.course.enrollments.all()
        
        channel_layer = get_channel_layer()

        for enrollment in enrolled_students:
            group_name = f'notifications_{enrollment.student.username}'
            message = f"New material added to your course: {instance.course.title}."
            
            async_to_sync(channel_layer.group_send)(
                group_name,
                {
                    'type': 'user_notification',
                    'notification_type': 'new_material',
                    'message': message
                }
            )
