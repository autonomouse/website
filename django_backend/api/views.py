from datetime import datetime
from django.shortcuts import render
from rest_framework import viewsets, filters, permissions
from api import models, serializers

class PageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows pages to be viewed or edited.
    """
    queryset = models.Page.objects.all()
    serializer_class = serializers.PageSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('uuid', 'name', 'slug', 'priority', )


class SectionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows sections to be viewed or edited.
    """
    queryset = models.Section.objects.all()
    serializer_class = serializers.SectionSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = (
        'uuid', 'name', 'priority', 'page__name', 'page__slug', 'page__uuid', )


class StatementViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows statements to be viewed or edited.
    """
    queryset = models.Statement.objects.all().order_by('priority')
    serializer_class = serializers.StatementSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = (
        'uuid', 'priority', 'title', 'text', 'section__name', 'section__uuid', )
