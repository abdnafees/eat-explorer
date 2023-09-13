import 'bootstrap/dist/css/bootstrap.min.css';

const RestaurantCard = ({restaurant}) => {

    const tempDiv = document.createElement('div');
    tempDiv.innerHTML = restaurant.photos[0].html_attributions;

    // Get the anchor tag from the temporary div
    const anchorTag = tempDiv.querySelector('a');
    console.log(anchorTag);
    return (
        <div className="card mb-4">
            {/* Display photos from the backend */}
            {restaurant.photos && restaurant.photos.length > 0 ? (
                <img src={anchorTag.href} className="card-img-top" alt={restaurant.name} crossOrigin="anonymous"/>
            ) : (
                <div className="no-photo-placeholder">
                    No Photo Available
                </div>
            )}
            <div className="card-body">
                <h5 className="card-title">{restaurant.name}</h5>
                <p className="card-text">
                    <strong>Rating:</strong> {restaurant.rating}
                    <br/>
                    <strong>Total Ratings:</strong> {restaurant.user_ratings_total}
                    <br/>
                    <strong>Address:</strong> {restaurant.vicinity}
                </p>
            </div>
        </div>
    );
};

export default RestaurantCard;
