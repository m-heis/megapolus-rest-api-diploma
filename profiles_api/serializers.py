from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)


class FamilySerializer(serializers.Serializer):
    """Serializes my age"""
    age = serializers.IntegerField(max_value=21, min_value=21)
