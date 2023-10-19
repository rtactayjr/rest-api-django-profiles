from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    """
        breakdown of get function:

        self = required argument for class based functions

        request = s an object representing the incoming HTTP request.
        It contains information about the client's request, including the URL, HTTP method, headers, and any data that was sent with the request.

        format = This is an optional parameter that allows you to specify the desired response format.
        Depending on the request and your view's implementation, you may want to return different response formats, such as HTML, JSON, XML, or others
    """
    def get(self, request, format=None):
        """Returns a list of APIView features"""

        #  lists
        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs',
        ]

        # return statement
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
        # key:value, key:value
