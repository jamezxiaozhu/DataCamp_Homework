// Assign the data from `data.js` to a descriptive variable
var sightings = data;

// Select the button
var button = d3.select("#filter-btn");

button.on("click", function() {
    
    var tbody = d3.select("tbody");

    //clear original table
    tbody.html("");

    // Select the input element and get the raw HTML node
    var inputElement = d3.select("#datetime");
  
    // Get the value property of the input element
    var inputValue = inputElement.property("value");
  
    console.log(inputValue);
    console.log(sightings);
    console.log(typeof inputValue);

    var filteredData = sightings.filter(sighting => Date.parse(sighting.datetime) === Date.parse(inputValue));
  
    console.log(filteredData);

    //get info from dataset and turn into table
    filteredData.forEach((ufoIncident) => {
        var row = tbody.append("tr");
        Object.entries(ufoIncident).forEach(([key, value]) => {
          var cell = row.append("td");
          cell.text(value);
        });
      });


});