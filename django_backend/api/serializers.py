from rest_framework import serializers
from api import models


class PageSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Page
        fields = ('uuid', 'name', 'slug')


class SectionSerializer(serializers.HyperlinkedModelSerializer):
    page = PageSerializer()

    class Meta:
        model = models.Section
        fields = ('uuid', 'name', 'page')


class StatementSerializer(serializers.HyperlinkedModelSerializer):
    section = SectionSerializer()

    class Meta:
        model = models.Statement
        fields = ('uuid', 'priority', 'title', 'text', 'section')
