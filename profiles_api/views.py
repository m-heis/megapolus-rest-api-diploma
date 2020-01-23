from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over you application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})


class SakenApiView(APIView):
    """Saken API View"""

    def get(self, request, format=None):
        """Returns a list of Saken's characters"""
        an_apiview = [
            'Not funny',
            'Want to wake early but can not',
            'Likes learning new things',
        ]

        return Response({'message': 'Saken Bolatzhanuly', 'an_apiview': an_apiview})


class FamilyApiView(APIView):
    """My Family Api View"""

    serializer_class = serializers.FamilySerializer

    def get(self, request, format=None):
        """Returns a list of names of my family"""
        an_apiview = [
            'Bolatzhan',
            'Anarkul',
            'Saken'
        ]

        return Response({'message': 'Hello form my famly', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            age = serializer.validated_data.get('age')
            message = f'I am {age}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
