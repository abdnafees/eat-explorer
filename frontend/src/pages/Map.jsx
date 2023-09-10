import {GoogleMap, LoadScript, Marker} from '@react-google-maps/api';
import {useEffect, useState} from "react";

// Replace with your own Google Maps API Key
const apiKey = 'AIzaSyCQ9bqrZcaPrIMRE8T3IgtXNVeocvr5tfk';

const Map = ({onMarkerChange}) => {

    const [currentPosition, setCurrentPosition] = useState({
        lat: 31.5204,
        lng: 74.3587
    });

    useEffect(() => {
        // Use the browser's geolocation to get the user's current position
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(
                (position) => {
                    const lat = position.coords.latitude;
                    const lng = position.coords.longitude;
                    setCurrentPosition({lat, lng});

                    // Notify the parent component about the marker change
                    onMarkerChange({lat, lng});
                },
                (error) => {
                    console.error('Error getting geolocation:', error);
                }
            );
        } else {
            console.error('Geolocation is not supported by this browser.');
        }
    }, [onMarkerChange]);
    const containerStyle = {
        width: '100%',
        height: '400px',
    };

    // const center = {
    //     lat: 31.5204, // Replace with your desired latitude
    //     lng: 74.3587, // Replace with your desired longitude
    // };

    return (
        <LoadScript googleMapsApiKey={apiKey}>
            <GoogleMap
                mapContainerStyle={containerStyle}
                center={currentPosition} // Default to Lahore City if geolocation is not available
                zoom={15} // Adjust the zoom level as needed
            >
                {currentPosition && (
                    <Marker
                        position={currentPosition}
                        icon={"https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png"}
                        draggable={true}
                        onDragEnd={({latLng}) => {
                            const lat = latLng.lat();
                            const lng = latLng.lng();
                            setCurrentPosition({lat, lng});

                            // Notify the parent component about the marker change
                            onMarkerChange({lat, lng});
                        }}
                    />
                )}
            </GoogleMap>
        </LoadScript>
    );
};


export default Map;
