from rest_framework import generics, permissions
from ..serializers import LinkSerializer


class FeaturedMediaAPIViewSet(generics.ListAPIView, 
    generics.DestroyAPIView, generics.CreateAPIView):
    
    serializer_class = LinkSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
