#  api_views.py
#
#  by: Islam Diaa
#       17 Jul 2016
#

from .models import Users, Timeline, Replies, Likes, Dislikes, Follow
from rest_framework import generics
from .serializers import UsersSerializer, TimelineSerializer, RepliesSerializer

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

# from rest_framework.authtoken.models import Token
# from rest_framework.exceptions import ParseError
# from rest_framework import status
# from django.contrib.auth.models import User

class AuthView(APIView):
    """
    Authentication is needed for this methods
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        # print(request.user)
        return Response({'detail': "I suppose you are authenticated"})

#
# class TestView(APIView):
#     def get(self, request, format=None):
#         return Response({'detail': "GET Response"})
#
#     def post(self, request, format=None):
#         try:
#             data = request.DATA
#         except ParseError as error:
#             return Response(
#                 'Invalid JSON - {0}'.format(error.detail),
#                 status=status.HTTP_400_BAD_REQUEST
#             )
#         if "user" not in data or "password" not in data:
#             return Response(
#                 'Wrong credentials',
#                 status=status.HTTP_401_UNAUTHORIZED
#             )
#
#         user = User.objects.first()
#         if not user:
#             return Response(
#                 'No default user, please create one',
#                 status=status.HTTP_404_NOT_FOUND
#             )
#
#         token = Token.objects.get_or_create(user=user)
#
#         return Response({'detail': 'POST answer', 'token': token[0].key})


# -- API Listing -- #
class UsersList(generics.ListCreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class TimelineList(generics.ListCreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Timeline.objects.all()
    serializer_class = TimelineSerializer

# -- End API listing -- #


# -- API Details -- #
class UsersDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class TimelineDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Timeline.objects.all()
    serializer_class = TimelineSerializer

# -- End API Details -- #