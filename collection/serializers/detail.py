from rest_framework import serializers
from ..models import Collection, Item

class ItemSerializer(serializers.ModelSerializer):
    
    def validate(self, data):
        instance = getattr(self, 'instance', None)
        item_type = data.get('item_type') or (instance.item_type if instance else None)
        details = data.get('details') or (instance.details if instance else {})

        REQUIRED_FIELDS = {
            'book': ['author', 'pages'],
            'music': ['artist'],
            'movie': ['director'],
            'game' : ['platform'],
            'restaurant' : ['cuisine', 'location'],
            'travel' : ['country'],
            'workout' : ['exercise'],
            'product' : ['brand'],
            'event' : ['event_name'],
        }

        required = REQUIRED_FIELDS.get(item_type, [])
        missing = [field for field in required if field not in details]

        if missing:
            raise serializers.ValidationError({
                'details': f'Missing required fields for {item_type}: {missing}'
            })
        return data
    
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