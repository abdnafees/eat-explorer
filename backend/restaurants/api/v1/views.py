# Create your views here.

from django.db.models import Q
from rest_framework import filters
from rest_framework.generics import ListAPIView

from backend.restaurants.api.v1.models import Restaurant
from backend.restaurants.api.v1.paginations import CustomPagination
from backend.restaurants.api.v1.serializers import RestaurantSerializer
from backend.restaurants.api.v1.utils import create_restaurants


class RestaurantListAPIView(ListAPIView):
    serializer_class = RestaurantSerializer
    pagination_class = CustomPagination  # Use the custom pagination class

    # Add a filter backend to enable keyword and location filtering
    filter_backends = [filters.SearchFilter]

    # Define the fields you want to filter on (keywords and location)
    search_fields = [
        "name",
        "vicinity",
        "types",
    ]  # Add any other fields you want to search on

    def get_serializer_context(self):
        """
        Override the serializer context to customize it for GET requests.
        """
        # Check if it's a GET request
        if self.request.method == "GET":
            # Define a custom context that doesn't require certain fields
            context = {
                "exclude_fields": [
                    "geometry",
                    "icon",
                    "icon_background_color",
                    "place_id",
                    "reference",
                ]
            }
            return context
        # For other request methods (e.g., POST), use the default context
        return super().get_serializer_context()

    def get_queryset(self):
        # Retrieve the user-provided search parameters from the request
        query_params = RestaurantSerializer(data=self.request.query_params)
        query_params.is_valid(raise_exception=True)
        keywords = self.request.query_params.get("keywords", "")
        latitude = self.request.query_params.get("latitude", None)
        longitude = self.request.query_params.get("longitude", None)
        radius = self.request.query_params.get("radiusInMeters", None)

        restaurants = create_restaurants(latitude, longitude, radius, keywords)

        # Create a queryset that includes keyword filtering
        if restaurants["status"] == 201:
            queryset = Restaurant.objects.all()

        # Apply keyword filtering
        if keywords:
            # Use Q objects for OR filtering on multiple fields
            queryset = queryset.filter(
                Q(name__icontains=keywords)
                | Q(vicinity__icontains=keywords)
                | Q(types__icontains=keywords)
            )

        # Adjust the queryset based on your filtering or ordering requirements
        return queryset.order_by("name")
