from django.core.exceptions import ValidationError
from django_filters import rest_framework as filters

from .models import TableEntry


class DynamicFilter(filters.FilterSet):
    filter_value = filters.CharFilter(method='filter_by_field')

    class Meta:
        model = TableEntry
        fields = ['date', 'name', 'quantity', 'distance']

    def filter_by_field(self, queryset, name, value):
        # Получаем колонку для фильтрации из параметра запроса
        filter_field = self.request.query_params.get('filter_field')
        filter_condition = self.request.query_params.get('filter_condition')

        if not filter_field or not filter_condition:
            return queryset

        # Валидируем колонку и условие
        if filter_field not in ['date', 'name', 'quantity', 'distance']:
            raise ValidationError(f"Invalid filter field: {filter_field}")

        if filter_condition not in ['exact', 'icontains', 'gt', 'lt']:
            raise ValidationError(f"Invalid filter condition: {filter_condition}")

        # Формируем динамическое имя фильтра
        filter_param = f"{filter_field}__{filter_condition}"

        # Применяем фильтрацию к queryset
        return queryset.filter(**{filter_param: value})
