'''
The serializers module contains classes and functions that allow you to define how your data objects
(typically Python objects or Django models) should be converted to JSON or other data formats
when sending responses from your API (serialization), and how incoming data should be converted into Python objects (deserialization).
'''

from rest_framework import serializers


class HelloSerializer(serializers.Serializer):

    """Serializes a name field for testing out APIView"""
    name = serializers.CharField(max_length=10)
