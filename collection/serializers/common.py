from rest_framework import serializers
from ..models import Collection

class CollectionSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Collection
        fields = ('id', 'title', 'description', 'image', 'created_at', 'updated_at', 'user', 'username')
        read_only_fields = ('id', 'created_at', 'updated_at', 'user')