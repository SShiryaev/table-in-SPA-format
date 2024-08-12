from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter

from table.filters import DynamicFilter
from table.models import TableEntry
from table.paginators import TablePaginator
from table.serializers import TableSerializer


class TableViewSet(viewsets.ModelViewSet):
    serializer_class = TableSerializer
    queryset = TableEntry.objects.all()
    pagination_class = TablePaginator
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = DynamicFilter
    ordering_fields = ('name', 'quantity', 'distance',)
