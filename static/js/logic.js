var map = L.map('map').setView([32.7157, -117.1611], 10);
var markers = L.markerClusterGroup(); // Create a marker cluster group

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

const apiEndpoint = '/airbnb';


function fetchDataAndCreateMarkers() {
  fetch(apiEndpoint)
    .then((response) => response.json())
    .then((data) => {
      data.forEach(item => {
        var marker = L.marker([item.latitude, item.longitude]); // Create a marker
        // Customize the marker as needed, e.g., add pop-up content
        marker.bindPopup(`<strong>${item.price}</strong><br>Neighbourhood: ${item.neighbourhood}`);
        markers.addLayer(marker); // Add the marker to the marker cluster group

      });

      // Add the marker cluster layer to the map
      map.addLayer(markers);
      // Process and use the data as needed
      console.log(data); // Example: Log the data to the console
    })
    .catch((error) => {
      console.error('Error fetching data:', error);
    });
}
// Call the fetchData function to retrieve data from the new endpoint
fetchDataAndCreateMarkers();

const columnSelect = document.getElementById('column-select');
columnSelect.addEventListener('change', (event) => {
  const selectedColumn = event.target.value;
  fetchCrimeDataAndCreateBarChart(selectedColumn);
});

function fetchCrimeDataAndCreateBarChart(selectedColumn) {
  const secondapiEndpoint = `/crime?column=${selectedColumn}`;
  fetch(secondapiEndpoint)
    .then((response) => response.json())
    .then((data) => {
      const labels = data.map((item) => item.Crime);
      const values = data.map((item) => item[selectedColumn]);

      const barData = [{
        x: labels,
        y: values,
        type: 'bar',
      }];

      const layout = {
        title: `Crime Data for ${selectedColumn} from July 2022 to July 2023`,
        xaxis: { title: 'Crime Type'},
        yaxis: { title: selectedColumn}
      };

      Plotly.newPlot('bar-chart', barData, layout);
    })
    .catch((error) => {
      console.error('Error fetching crime data:', error);
    });
}

const pieColumn = 'Day_of_week'

function fetchPieDataCreatePieChart() {
  
  const piechartEndpoint = '/car_crash';

  fetch(piechartEndpoint)
    .then((response) => response.json())
    .then((data) => {
      
      const valueCounts = [0, 0, 0, 0, 0, 0, 0];
      data.forEach((item) => {
        const value = item.Day_of_week;
        if (value >= 1 && value <= 7) {
          valueCounts[value -1]++
        }
      });

      const labels = ['1: Monday', '2: Tuesday', '3: Wednesday', '4: Thursday', '5: Friday', '6: Saturday', '7: Sunday'];
      
      const values = valueCounts

      const pieData = [{
        labels: labels,
        values: values,
        type: 'pie',
      }];

      const layout = {
        title: 'Pie Chart'
      }

      Plotly.newPlot('pie-chart', pieData, layout);
    })
    .catch((error) => {
      console.error('Error fetching pie chart data:', error);
    });
}

fetchPieDataCreatePieChart();
