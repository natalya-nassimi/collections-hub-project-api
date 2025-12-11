from rest_framework import serializers
from django.contrib.auth import password_validation, hashers
from ..models import User

class SignUpSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'confirm_password')
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def validate(self, data):
        password = data.get('password')
        confirm_password = data.pop('confirm_password')

        if password != confirm_password:
            raise serializers.ValidationError({
                'password': 'Passwords do not match'
            })
        
        password_validation.validate_password(password)
        data['password'] = hashers.make_password(password)

        return data