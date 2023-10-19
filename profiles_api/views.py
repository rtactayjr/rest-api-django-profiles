from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status

from . import serializers

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
