function Pagination({prevPage, nextPage, onPageChange}) {
    const handlePrevPage = () => {
        onPageChange(prevPage);
    };

    const handleNextPage = () => {
        onPageChange(nextPage);
    };

    return (
        <div className="btn-group" style={{padding: 20 + 'px'}}>
            <button onClick={handlePrevPage}>Previous</button>
            <button onClick={handleNextPage}>Next</button>
        </div>
    );
}

export default Pagination;
