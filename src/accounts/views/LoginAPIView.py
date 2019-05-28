from ..serializers import LoginSerializer, UserSerializer
from rest_framework import generics, permissions, serializers, status
from django.contrib.auth.signals import user_logged_in, user_logged_out
from rest_framework.response import Response
from knox.models import AuthToken


class LoginAPIView(generics.GenericAPIView):
    
    serializer_class = LoginSerializer
    permissions_classes = [
        permissions.AllowAny
    ]

    def post(self, request, *a, **kw):
        serilizer = self.get_serializer(data=request.data)
        try:
            serilizer.is_valid(raise_exception=True)
            user = serilizer.validated_data
            user_logged_in.send(sender=request.user.__class__,
                             request=request, user=request.user)
            return Response({
                "data": {
                    "user": UserSerializer(user, context=self.get_serializer_context()).data,
                    "token": f'{AuthToken.objects.create(user)[1]}'
                }
            })
        except serializers.ValidationError as err:
            return Response({
                "data": {
                },
                "errors": {
                    "message": "Invalid credentionals!",
                    "detail": err.detail
                }
            }, status.HTTP_403_FORBIDDEN)
