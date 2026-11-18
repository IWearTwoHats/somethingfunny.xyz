// The best JavaScript you'll ever see

function getDropdownIndex(collection, value) {
	let i = 0;
	for (cval of collection.options) {
		if (cval.value == value) return i;
		i++;
	}
}

const searchBar = document.getElementById('search-bar');
const categoryDropdown = document.getElementById('search-category');
const searchButton = document.getElementById('search-button');
const queryParams = new URLSearchParams(window.location.search);

const searched = queryParams.has('q') & queryParams.get('q') != '';

// Set tabIndex
searchBar.tabIndex = 1;
if (categoryDropdown !== null) {
	categoryDropdown.tabIndex = 2;
} else {
	console.warn('No dropdown for search');
}
if (searchButton !== null) {
	searchButton.tabIndex = 3;
} else console.warn('No search button');

if (searched) {
	// Set elements to existing values.
	searchBar.value = queryParams.get('q');
	categoryDropdown.selectedIndex = getDropdownIndex(categoryDropdown, queryParams.get('category'));
}
searchBar.select();
