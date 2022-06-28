from rest_framework import permissions, viewsets

from core.models import Person
from core.serializers import PersonSerializer


class PersonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Person.objects.all().order_by("last_name", "first_name", "date_of_birth")
    serializer_class = PersonSerializer
    permission_classes = [permissions.IsAuthenticated]
