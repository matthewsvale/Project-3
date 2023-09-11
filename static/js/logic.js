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

// Function that fetches the data from the crime_data table
function fetchPieDataCreatePieChart() {
  // Defines API endpoint for the Crash_Locations table data
  const piechartEndpoint = '/car_crash';
  fetch(piechartEndpoint)
    .then((response) => response.json())
    .then((data) => {

      // Creates the headers for the pie chart
      const chartData = [['Day', 'Count']];
      // Needed for the sidebar to show what each number represents and to count the number of times the day is found in the column
      const dayLabels = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];
      const dayCounts = {
        Monday: 0,
        Tuesday: 0,
        Wednesday: 0,
        Thursday: 0,
        Friday: 0,
        Saturday: 0,
        Sunday: 0,
      };
      
      // Iterates through the column to count the amount of times the number that represents the day of the week appears 
      data.forEach((item) => {
        const dayOfWeek = dayLabels[item.Day_of_week - 1];
        dayCounts[dayOfWeek]++ 
      });

      // Turns dayCounts into an array and appends to chartData
      Object.entries(dayCounts).forEach(([dayOfWeek, count]) => {
        chartData.push([dayOfWeek, count]);
      });

      // Used to load Google Charts js library and calls the GooglePieChart function
      google.charts.load('current', {'packages': ['corechart']});
      google.charts.setOnLoadCallback(() => GooglePieChart(chartData));
    })
    .catch((error) => {
      console.error('Error fetching pie chart data:', error);
    });

}

// Function converting chartData into a DataTable
function GooglePieChart(chartData) {
  const data = google.visualization.arrayToDataTable(chartData);

  const options = {
    title: 'Pie Chart',
  };

  // Associates PieChart with google-pie-chart and draws it
  const chart = new google.visualization.PieChart(document.getElementById('google-pie-chart'));
  chart.draw(data, options);
}

// Loads the Google Charts js library and starts up the function
google.charts.load('current', {'packages': ['corechart']});
fetchPieDataCreatePieChart();
