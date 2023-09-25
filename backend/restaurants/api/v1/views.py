# Create your views here.
import googlemaps
from decouple import config  # Import config from decouple to read environment variables
from django.db.models import Q
from rest_framework import filters
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from backend.restaurants.api.v1.models import Restaurant, Location, Geometry, Photo
from backend.restaurants.api.v1.serializers import RestaurantSerializer


class RestaurantCreateAPIView(CreateAPIView):
    serializer_class = RestaurantSerializer

    def create(self, request, *args, **kwargs):
        # Get the data from the request
        data = request.data
        latitude = float(data.get("latitude"))
        longitude = float(data.get("longitude"))
        keywords = data.get("keywords")
        radius = int(data.get("radiusInMeters"))  # In meters

        # Load your Maps API key from the .env file
        maps_api_key = config(
            "GOOGLE_MAPS_API_KEY"
        )  # Define MAPS_API_KEY in your .env file

        gmaps = googlemaps.Client(key=maps_api_key)

        # Perform a Nearby Search using the Places API
        location = (latitude, longitude)
        places_result = gmaps.places_nearby(
            location=location, radius=radius, keyword=keywords, language="en"
        )

        if places_result["status"] == "OK":
            # Successfully retrieved results
            results = places_result["results"]
            # Parse and save restaurant data
            for result in results:
                # Create Location instance
                location_data = {
                    "lat": result.get("geometry", {}).get("location", {}).get("lat"),
                    "lng": result.get("geometry", {}).get("location", {}).get("lng"),
                }
                location_instance = Location.objects.create(**location_data)

                # Create Geometry instance and associate it with Location
                geometry_instance = Geometry.objects.create(location=location_instance)

                # Create Photo instances and associate them with the Restaurant
                photos_data = [
                    {
                        "height": photo.get("height"),
                        "html_attributions": photo.get("html_attributions"),
                        "photo_reference": photo.get("photo_reference"),
                        "width": photo.get("width"),
                    }
                    for photo in result.get("photos", [])
                ]
                photos_instances = Photo.objects.bulk_create(
                    [Photo(**photo_data) for photo_data in photos_data]
                )
                restaurant_data = {
                    "name": result.get("name"),
                    "business_status": result.get("business_status"),
                    "geometry": geometry_instance,
                    "icon": result.get("icon"),
                    "icon_background_color": result.get("icon_background_color"),
                    "rating": result.get("rating"),
                    "place_id": result.get("place_id"),
                    "vicinity": result.get("vicinity"),
                    "types": result.get("types"),
                    "user_ratings_total": result.get("user_ratings_total"),
                }

                # Create or update the Restaurant instance
                restaurant, created = Restaurant.objects.update_or_create(
                    place_id=restaurant_data["place_id"], defaults=restaurant_data
                )
                # Associate photos with the Restaurant
                restaurant.photos.set(photos_instances)
            return Response(
                {
                    "message": "Restaurants data saved successfully",
                },
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(
                {"error": "Invalid request to Places API"},
                status=status.HTTP_400_BAD_REQUEST,
            )


class CustomPagination(PageNumberPagination):
    page_size = 9  # Adjust the page size as needed
    page_size_query_param = "page_size"
    max_page_size = 100  # Set the maximum page size if desired


class RestaurantDetailsView(ListAPIView):
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
        keywords = self.request.query_params.get("keywords", "")
        latitude = self.request.query_params.get("latitude", None)
        longitude = self.request.query_params.get("longitude", None)
        radius = self.request.query_params.get("radiusInMeters", None)

        # Create a queryset that includes keyword and location filtering
        queryset = Restaurant.objects.all()

        # Apply keyword filtering
        if keywords:
            # Use Q objects for OR filtering on multiple fields
            queryset = queryset.filter(
                Q(name__icontains=keywords)
                | Q(vicinity__icontains=keywords)
                | Q(types__icontains=keywords)
            )

        # Apply location filtering if latitude, longitude, and radius are provided
        if latitude is not None and longitude is not None and radius is not None:
            # Create a point representing the user's location
            queryset = queryset.filter(
                geometry__location__lat__range=(
                    float(latitude)
                    - (float(radius) / 1000),  # Convert radius to kilometers
                    float(latitude) + (float(radius) / 1000),
                ),
                geometry__location__lng__range=(
                    float(longitude)
                    - (float(radius) / 1000),  # Convert radius to kilometers
                    float(longitude) + (float(radius) / 1000),
                ),
            )

        # Adjust the queryset based on your filtering or ordering requirements
        return queryset.order_by("name")
