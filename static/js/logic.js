var map = L.map('map').setView([32.7157, -117.1611], 10);


L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

fetch('/markers')

    .then(response => response.json())
    .then(data => {
        // Loop through the marker data and add markers to the map
        console.log(data)
        data.forEach(marker => {
            L.marker([marker.latitude, marker.longitude])
                .addTo(map)
                .bindPopup(marker.neighbourhood);  // Show marker name as a popup
        });
    });