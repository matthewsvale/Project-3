var map = L.map('map').setView([32.7157, -117.1611], 10);


L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);


const apiEndpoint = '/airbnb';

function fetchData() {
    fetch(apiEndpoint)
      .then((response) => response.json())
      .then((data) => {
        data.forEach(item => {
            var marker = L.marker([item.latitude, item.longitude]).addTo(map);
            // Customize the marker as needed, e.g., add pop-up content
            marker.bindPopup(`<strong>${item.price}</strong><br>Neighbourhood: ${item.neighbourhood}`);

        });
        // Process and use the data as needed
        console.log(data); // Example: Log the data to the console
      })
      .catch((error) => {
        console.error('Error fetching data:', error);
      });
  }
  
  // Call the fetchData function to retrieve data from the new endpoint
  fetchData();