from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import IssueSerializer
from .models import Issue

class IssueViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

    @action(detail=True, methods=['post'])
    def increment_visit_count(self, request, pk=None, str=None):
        issue = self.get_object()
        issue.visit_count += 1
        issue.save()
        return Response({'message': str(pk) +'방문'})