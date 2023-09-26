from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    page_size = 9  # Adjust the page size as needed
    page_size_query_param = "page_size"
    max_page_size = 100  # Set the maximum page size if desired
