
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import viewsets
from rest_framework import status
from rest_framework import filters


from . import serializers
from . import models
from . import permissions


class HelloApiView(APIView):
    """Test API View"""

    # variable
    serializer_class =  serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""

        #  lists
        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
            # key:value, key:value

    def post(self, request):
        """ Create a hello message with our name """

        # variable
        serializer = self.serializer_class(data=request.data)

        # validate serializers
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'

            return Response({'message':message})
            #'key':value

        # throw an error if input is invalid
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Update an Object, pk = primary key
    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    # Update an Object, Only update fields provided in the request
    def patch(self, request, pk=None):
        """Handle partial update of object"""
        return Response({'method': 'PATCH'})

    # Remove/Delete an object from the database
    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})


# create new class
class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message."""
        ...

    def create(self, request):
        """Create a new hello message."""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""

        return Response({'http_method': 'DELETE'})


# create new class
class UserProfileViewSet(viewsets.ModelViewSet):

    """Handle creating, creating and updating profiles"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()

    authentication_classes = (TokenAuthentication,) #created as tuple using ,
    permission_classes = (permissions.UpdateOwnProfile,)  #created as tuple using ,

    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class UserLoginApiView(ObtainAuthToken):
   """Handle creating user authentication tokens"""
   renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)
