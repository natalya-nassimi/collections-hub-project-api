from rest_framework import serializers
from django.contrib.auth import password_validation, hashers, authenticate
from ..models import User
from rest_framework.exceptions import AuthenticationFailed

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
    
class SignInSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(
            username = data['username'],
            password = data['password']
        )

        if not user:
            raise AuthenticationFailed('Invalid username or password')
        
        data['user'] = user
        return data