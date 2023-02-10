from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer, UserSerializerForQueries


# Create your views here.
class CreateUserAPIView(CreateAPIView):
    serializer_class = UserSerializer


class UserDetailsAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, *args, **kwargs):
        user_serializer = UserSerializerForQueries(self.request.user)
        return Response(user_serializer.data, status=status.HTTP_200_OK)
