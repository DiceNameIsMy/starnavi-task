from datetime import datetime

from rest_framework.filters import BaseFilterBackend


class DateFilter(BaseFilterBackend):
    """ Custom filtering for slicing dates
    Add "date_fields" to view to slice these dates
    """

    def get_date_fields(self, view, request) -> list:
        return getattr(view, 'date_fields', [])

    def filter_queryset(self, request, queryset, view):
        date_fields = self.get_date_fields(view, request)

        for field in date_fields:
            if field + "_start" in request.query_params:
                start_date = datetime.strptime(request.query_params.get(field + "_start"), "%Y-%m-%d")
                queryset = queryset.filter(**{f"{field}__gte": start_date})

            if field + "_end" in request.query_params:
                end_date = datetime.strptime(request.query_params.get(field + "_end"), "%Y-%m-%d")
                queryset = queryset.filter(**{f"{field}__lte": end_date})

        return queryset