from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from django.urls import reverse
from .models import CustomUser
from django.core.exceptions import ValidationError
from django.core.files.storage import default_storage
import os

class CustomUserSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = CustomUser
        fields = ['url', 'id', 'username', 'password', 'email', 'full_name', 'role', 'photo', 'is_active']
        # Set fields to optional to allow for partial update
        extra_kwargs = {
            'password': {'write_only': True, 'required': False},
            'is_active': {'read_only': True},
            'email': {'required': False},
            'full_name': {'required': False},
            'role': {'required': False},
            'photo': {'required': False},
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserSerializer, self).__init__(*args, **kwargs)
        # If creating a new user all fields are set to required
        if not self.instance:
            self.fields['photo'].required = True
            self.fields['email'].required = True
            self.fields['password'].required = True
            self.fields['full_name'].required = True
            self.fields['role'].required = True
            

    # Hash the password upon creation and set is_active to true
    def create(self, validated_data):
        if 'photo' not in validated_data:
            raise serializers.ValidationError({"photo": "This field is required."})
        validated_data['password'] = make_password(validated_data.get('password'))
        validated_data['is_active'] = True
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # Hash the password
        password = validated_data.pop('password', None)
        if password:
            instance.set_password(password)

        # If there is a new photo the old photo will be removed from the media folder
        new_photo = validated_data.get('photo', None)
        if new_photo and instance.photo:
            if os.path.isfile(instance.photo.path):
                os.remove(instance.photo.path)
        
        # If no new photo is chosen the old photo will be used
        if 'photo' in validated_data and not validated_data['photo']:
            validated_data.pop('photo')

        return super().update(instance, validated_data)

    # Ensure that emails are unique
    def validate_email(self, value):      
        if self.instance and self.instance.email == value:
            return value
        if CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already in use.")
        return value

    def get_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(reverse('users-detail', args=[obj.pk]))