from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination,CursorPagination


class pagination_page(PageNumberPagination):
    max_page_size=10
    page_size=2
    page_query_param='mypage'
    page_size_query_param='size'


class limitoffset_pagination(LimitOffsetPagination):
        default_limit=1
        limit_query_param='limit'
        offset_query_param='offset'





