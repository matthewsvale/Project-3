// Gets a Leaflet map and points it towards San Diego
var map = L.map('map').setView([32.7157, -117.1611], 10);
var markers = L.markerClusterGroup();

// Gets OpenStreeMap for base layer
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

// Defines API endpoint for Airbnb data
const apiEndpoint = '/airbnb';


// Function that fetches the airbnb table data and creates markers
function fetchDataAndCreateMarkers() {
  fetch(apiEndpoint)
    .then((response) => response.json())
    .then((data) => {
      data.forEach(item => {
        // Creates markers
        var marker = L.marker([item.latitude, item.longitude]); 

        // Adds things to the pop up, such as price and neighbourhood name then adds to mark cluster group
        marker.bindPopup(`<strong>${item.price}</strong><br>Neighbourhood: ${item.neighbourhood}`);
        markers.addLayer(marker);

      });

      // Add the marker cluster layer to the map
      map.addLayer(markers);

      console.log(data);
    })
    .catch((error) => {
      console.error('Error fetching data:', error);
    });
}
fetchDataAndCreateMarkers();

// Gets the column select element from DOM
const columnSelect = document.getElementById('column-select');

// Event listner 
columnSelect.addEventListener('change', (event) => {
  const selectedColumn = event.target.value;
  fetchCrimeDataAndCreateBarChart(selectedColumn);
});

// Function that fetches the crime_data table data for the user selected column
function fetchCrimeDataAndCreateBarChart(selectedColumn) {

  // Defines this API endpoint that will fetch the data from the selected column
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
      
      // Use Plotly to create the bar graph
      Plotly.newPlot('bar-chart', barData, layout);
    })
    .catch((error) => {
      console.error('Error fetching crime data:', error);
    });
}

// Define column we want to use for the pie chart
const pieColumn = 'Day_of_week'

function fetchPieDataCreatePieChart() {
  // Defines API endpoint for the Crash_Locations table data
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
      
      // Use Plotly to make the pie chart
      Plotly.newPlot('pie-chart', pieData, layout);
    })
    .catch((error) => {
      console.error('Error fetching pie chart data:', error);
    });
}
fetchPieDataCreatePieChart();
