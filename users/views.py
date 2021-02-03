from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response

from users.serializers import UserSerializer


# class CurrentUserView(APIView):
#     def get(self, request):
#         serializer = UserSerializer(request.user)
#
#         return Response(serializer.data)


class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):

    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


class UserRegister(CreateAPIView):
    serializer_class = UserSerializer
