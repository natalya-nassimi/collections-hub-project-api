from rest_framework import serializers
from ..models import Collection

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ('id', 'title', 'description', 'image', 'created_at', 'updated_at', 'user')
        read_only_fields = ('id', 'created_at', 'updated_at', 'user')