#  api_views.py
#
#  by: Islam Diaa
#       17 Jul 2016
#
from _elementtree import ParseError
from django.contrib.auth.models import User

from .models import Users, Timeline, Replies, Likes, Dislikes, Follow
from rest_framework import generics
from .serializers import UsersSerializer, TimelineSerializer, RepliesSerializer

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

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
        # username = request.user
        print(request.user)
        return Response({'token': "I suppose you are authenticated"})

    def post(self, request, format=None):
        token = Token.objects.get_or_create(user=request.user)
        user_data = Users.objects.get(user=request.user)
        if not user_data:
            return Response(
                'No default user, please create one',
                status=status.HTTP_404_NOT_FOUND
            )

        username = user_data.user.username
        email = user_data.email
        profile_picture = str(user_data.profile_picture)
        return Response({'username': username, 'email': email, 'token': token[0].key, 'profile_picture': profile_picture})
        # try:
        #     data = request.DATA
        # except ParseError as error:
        #     return Response(
        #         'Invalid JSON - {0}'.format(error.detail),
        #         status=status.HTTP_400_BAD_REQUEST
        #     )
        # if "user" not in data or "password" not in data:
        #     return Response(
        #         'Wrong credentials',
        #         status=status.HTTP_401_UNAUTHORIZED
        #     )
        #
        # user = User.objects.first()
        # if not user:
        #     return Response(
        #         'No default user, please create one',
        #         status=status.HTTP_404_NOT_FOUND
        #     )
        #
        # token = Token.objects.get_or_create(user=user)
        # return Response({'detail': 'POST answer', 'token': token[0].key})

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