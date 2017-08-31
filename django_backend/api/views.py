from datetime import datetime
from django.shortcuts import render
from rest_framework import viewsets, filters
from api import models, serializers


class SectionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows sections to be viewed or edited.
    """
    queryset = models.Section.objects.all()
    serializer_class = serializers.SectionSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('uuid', 'name', )


class StatementViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows statements to be viewed or edited.
    """
    queryset = models.Statement.objects.all().order_by('priority')
    serializer_class = serializers.StatementSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = (
        'uuid', 'priority', 'title', 'text', 'section__name', 'section__uuid')
