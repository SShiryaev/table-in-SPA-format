from rest_framework import serializers

from table.models import TableEntry


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableEntry
        fields = '__all__'
