from rest_framework import serializers

from core.models import Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"  # Could also be a list, e.g. ["first_name", "last_name", ...]
