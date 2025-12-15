from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework import status

from .models import Collection, Item
from .serializers.common import CollectionSerializer
from .serializers.detail import CollectionDetailSerializer, ItemSerializer
from .permissions import IsOwnerOrReadOnly

class CollectionListCreateView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        collections = Collection.objects.all().order_by('-created_at')
        serializer = CollectionSerializer(collections, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CollectionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class CollectionDetailView(APIView):
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            return Collection.objects.get(pk=pk)
        except Collection.DoesNotExist:
            raise NotFound('Collection not found')
        
    def get(self, request, pk):
        collection = self.get_object(pk)
        serializer = CollectionDetailSerializer(collection)
        return Response(serializer.data)
    
    def put(self, request, pk):
        collection = self.get_object(pk)
        self.check_object_permissions(request, collection)

        serializer = CollectionSerializer(collection, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, pk):
        collection = self.get_object(pk)
        self.check_object_permissions(request, collection)

        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class ItemCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, collection_id):
        try:
            collection = Collection.objects.get(id=collection_id)
        except Collection.DoesNotExist:
            raise NotFound('Collection not found')
        
        if collection.user != request.user:
            raise PermissionDenied('You do not own this collection')
        
        serializer = ItemSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(collection=collection)
        return Response(serializer.data)

class ItemDetailView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, collection_id, pk):
        try:
            return Item.objects.get(
                pk=pk,
                collection_id = collection_id
            )
        except Item.DoesNotExist:
            raise NotFound('Item not found in this collection')
        
    def put(self, request, collection_id, pk):
        item = self.get_object(collection_id, pk)

        if item.collection.user != request.user:
            raise PermissionDenied('You do not own this item')
        
        serializer = ItemSerializer(item, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, collection_id, pk):
        item = self.get_object(collection_id, pk)

        if item.collection.user != request.user:
            raise PermissionDenied('You do not own this item')
        
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)