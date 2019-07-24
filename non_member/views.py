from rest_framework import viewsets
from non_member.models import NonMember
from non_member.serializers import NonMemberSerializer


class NonMemberViewSet(viewsets.ModelViewSet):
    queryset = NonMember.objects.all()
    serializer_class = NonMemberSerializer
    lookup_field = 'no'
