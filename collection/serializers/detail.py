from rest_framework import serializers
from ..models import Collection, Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = (
            'id', 'title', 'item_type', 'image', 'link', 'details', 'created_at',
        )

class CollectionDetailSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = Collection
        fields = (
            'id', 'title', 'description', 'image', 'created_at', 'updated_at', 'items',
        )