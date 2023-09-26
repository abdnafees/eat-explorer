function InputForm({keywords, radiusInKilometers, handleKeywordsChange, handleRadiusChange, onSearch}) {
    return (
        <div className="input-group mb-3">
            <input
                type="text"
                className="form-control"
                placeholder="Enter keywords..."
                aria-label="Keywords"
                value={keywords}
                onChange={handleKeywordsChange}
            />
            <input
                type="number"
                className="form-control"
                placeholder="Enter search radius (in kilometers)"
                aria-label="Radius in Kilometers"
                value={radiusInKilometers}
                onChange={handleRadiusChange}
            />
            <button className="btn btn-primary" type="button" id="search-button" onClick={onSearch}>
                Search
            </button>
        </div>
    );
}

export default InputForm;
