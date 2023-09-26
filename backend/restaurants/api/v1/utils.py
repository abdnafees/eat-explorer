import googlemaps
from decouple import config  # Import config from decouple to read environment variables
from rest_framework import status
from rest_framework.response import Response

from backend.restaurants.api.v1.models import Restaurant, Location, Geometry, Photo


def create_restaurants(latitude, longitude, radius, keywords):
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
