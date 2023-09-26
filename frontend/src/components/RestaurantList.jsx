import RestaurantCard from "./RestaurantCard.jsx";

function RestaurantList({restaurants}) {
    return (
        <div className="row">
            {restaurants.map((restaurant) => (
                <div className="col-md-4" key={restaurant.id}>
                    <RestaurantCard restaurant={restaurant}/>
                </div>
            ))}
        </div>
    );
}

export default RestaurantList
