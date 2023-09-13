import './App.css';
import Map from "./pages/Map.jsx";
import 'bootstrap/dist/css/bootstrap.min.css';
import {useState} from "react";
import Header from "./components/Header.jsx";
import InputForm from "./components/InputForm.jsx";
import RestaurantList from "./components/RestaurantList.jsx";
import Pagination from "./components/Pagination.jsx";
import PrivacyAlert from "./components/PrivacyAlert.jsx";

function App() {

    const username = 'test1';
    const password = 'test123';

    // Encode the username and password in Base64 format
    const base64Credentials = btoa(`${username}:${password}`);
    const [latitude, setLatitude] = useState(null);
    const [longitude, setLongitude] = useState(null);
    const [keywords, setKeywords] = useState(''); // Add keywords state
    const [radiusInKilometers, setRadiusInKilometers] = useState('');
    const [restaurants, setRestaurants] = useState([]);
    const [nextPage, setNextPage] = useState(null);
    const [prevPage, setPrevPage] = useState(null);
    const [count, setCount] = useState(0);
    const [searchClicked, setSearchClicked] = useState(false);

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

    // Function to extract page number from URL
    const getPageNumberFromUrl = (url) => {
        const urlParams = new URLSearchParams(url);
        return urlParams.get('page');
    };


    const handleSearchClick = () => {
        setSearchClicked(true);
        // Now, trigger fetching restaurant data in the RestaurantList component
        searchRestaurants();
    };

    // Function to handle page changes
    const handlePageChange = (pageUrl) => {
        // Extract the page number from the pageUrl (e.g., 'http://localhost:8000/api/restaurants/details/?page=2')
        const pageNumber = getPageNumberFromUrl(pageUrl);

        if (pageNumber !== null) {
            // Call the fetchRestaurants function with the page number
            fetchRestaurants(`http://localhost:8000/api/restaurants/details/?page=${pageNumber}`);
        }
    };
    const radiusInMeters = radiusInKilometers * 1000;
    // Function to send a POST request for searching restaurants
    const searchRestaurants = () => {
        const apiUrl = "http://localhost:8000/api/restaurants/search/";


        // Send a POST request to search for restaurants
        fetch(apiUrl, {
            method: 'POST',
            headers: {
                // 'Authorization': `Basic ${base64Credentials}`,
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({latitude, longitude, keywords, radiusInMeters}),
        })
            .then((response) => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then((data) => {
                fetchRestaurants();
            })
            .catch((error) => {
                console.error('Error:', error);
            });
    };
    const fetchRestaurants = (pageUrl = null) => {
        let apiUrl = "http://localhost:8000/api/restaurants/details/";
        if (pageUrl) {
            apiUrl = pageUrl;
        }

        // Handle query parameters for keywords, latitude, longitude, and radiusInMeters
        const queryParams = [];
        if (keywords) {
            queryParams.push(`keywords=${encodeURIComponent(keywords)}`);
        }
        if (latitude) {
            queryParams.push(`latitude=${encodeURIComponent(latitude)}`);
        }
        if (longitude) {
            queryParams.push(`longitude=${encodeURIComponent(longitude)}`);
        }
        if (radiusInMeters) {
            queryParams.push(`radiusInMeters=${encodeURIComponent(radiusInMeters)}`);
        }

        // Append query parameters to the API URL
        if (queryParams.length > 0) {
            apiUrl += `?${queryParams.join("&")}`;
        }

        // Send a GET request to fetch restaurant details
        fetch(apiUrl)
            .then((response) => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then((data) => {
                // Update the restaurants state with detailed restaurant data
                if (Array.isArray(data.results)) {
                    setRestaurants(data.results);
                } else {
                    console.error('API response is not an array:', data.results);
                    setNextPage(data.next);
                    setPrevPage(data.previous);
                    setCount(data.count);
                }
            })
            .catch((error) => {
                console.error('Error:', error);
            });
        setSearchClicked(false);
    };


    return (
        <>
            <div className="container mt-5">
                <Header/>
                <InputForm
                    keywords={keywords}
                    radiusInKilometers={radiusInKilometers}
                    handleKeywordsChange={handleKeywordsChange}
                    handleRadiusChange={handleRadiusChange}
                    onSearch={handleSearchClick}
                />
                <PrivacyAlert/>
                <Map onMarkerChange={handleMapMarkerChange}/>

                {restaurants?.length > 0 && (
                    <RestaurantList
                        restaurants={restaurants}// Pass the fetchRestaurants function to fetch data
                    />
                )}
                <Pagination
                    prevPage={prevPage}
                    nextPage={nextPage}
                    onPageChange={handlePageChange}
                />
            </div>
        </>
    );
}

export default App;
