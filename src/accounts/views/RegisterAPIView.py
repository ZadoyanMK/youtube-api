from rest_framework import generics, permissions, exceptions
from rest_framework.response import Response
from knox.models import AuthToken
from ..serializers import UserSerializer, RegisterSerializer


class RegisterAPIView(generics.GenericAPIView):

    serializer_class = RegisterSerializer

    def post(self, request, *a, **k):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            user = serializer.save()

            return Response({
                "data": {
                    "user": UserSerializer(user, context=self.get_serializer_context()).data,
                    "token": f'{AuthToken.objects.create(user)[1]}'
                }
            })
        except exceptions.APIException as err:
            return Response({
                "data": {
                },
                "error": err.get_full_details()
            })
