from csv import field_size_limit
from typing_extensions import Required
from rest_framework import serializers

from shortener.models import Link

class LinkSerializer(serializers.ModelSerializer):
    hash = serializers.CharField(required=False)
    class Meta:
        model = Link
        fields = ('__all__')