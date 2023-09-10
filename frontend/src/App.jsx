import './App.css'
import Map from "./pages/Map.jsx";
import 'bootstrap/dist/css/bootstrap.min.css';
import {useState} from "react"; // Import Bootstrap CSS

function App() {
    const [latitude, setLatitude] = useState(null);
    const [longitude, setLongitude] = useState(null);
    const [keywords, setKeywords] = useState(''); // Add keywords state
    const [radiusInKilometers, setRadiusInKilometers] = useState('');


    // Function to handle latitude and longitude updates from the map component
    const handleMapMarkerChange = ({lat, lng}) => {
        setLatitude(lat);
        setLongitude(lng);
    };

    // Function to handle keyword input change
    const handleKeywordsChange = (event) => {
        setKeywords(event.target.value);
    };


    const handleRadiusChange = (event) => {
        setRadiusInKilometers(event.target.value);
    };

    const handleSearchClick = () => {
        // Check if latitude and longitude are available
        if (latitude !== null && longitude !== null) {
            const radiusInMeters = radiusInKilometers * 1000;
            // Send a POST request to your DRF API
            fetch('/api/location/detect/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({latitude, longitude, keywords, radiusInMeters}),
            })
                .then((response) => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    return response.json(); // Parse the JSON response
                })
                .then((data) => {
                    // Handle the response from your DRF API
                    console.log(data);
                })
                .catch((error) => {
                    // Handle errors
                    console.error('Error:', error);
                });
        } else {
            // Handle the case where latitude or longitude is missing
            console.error('Latitude or longitude is missing.');
        }
    };

    return (
        <>
            <div className="container mt-5">
                <h1 className="mb-6">Eat Explorer - Location Base Restaurant Recommendation</h1>

                {/* Input Field */}
                <div className="input-group mb-3">
                    <input
                        type="text"
                        className="form-control"
                        placeholder="Enter keywords..."
                        aria-label="Keywords"
                        aria-describedby="search-button"
                        value={keywords}
                        onChange={handleKeywordsChange} // Handle keyword input change
                    />
                    <input
                        type="number"
                        className="form-control"
                        placeholder="Enter search radius (in kilometers)"
                        value={radiusInKilometers}
                        onChange={handleRadiusChange}
                    />
                    <button className="btn btn-primary" type="button" id="search-button" onClick={handleSearchClick}>
                        Search
                    </button>
                </div>
                <div className="alert alert-info" role="alert">
                    Your privacy matters to us. We do not store your location data. We use your location only for
                    real-time restaurant recommendations and do not retain this information.
                </div>
                {/* Map Component */}
                <Map onMarkerChange={handleMapMarkerChange}/>

                {/* Additional content or components can be added here */}
            </div>
        </>
    )
}

export default App
