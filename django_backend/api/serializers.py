from rest_framework import serializers
from api import models


class SectionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Section
        fields = ('uuid', 'name')


class StatementSerializer(serializers.HyperlinkedModelSerializer):
    section = SectionSerializer()

    class Meta:
        model = models.Statement
        fields = ('uuid', 'priority', 'title', 'text', 'section')
