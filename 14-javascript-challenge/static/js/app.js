// Assign the data from `data.js` to a descriptive variable
var sightings = data;

// Select the button
var button = d3.select("#filter-btn");

button.on("click", function() {
    
    var tbody = d3.select("tbody");

    //clear original table
    tbody.html("");

    // Select the input element and get the raw HTML node
    var inputElementDate = d3.select("#datetime");
    var inputElementCity = d3.select("#city");
  
    // Get the value property of the input element
    var inputValueDate = inputElementDate.property("value");
    var inputValueCity = inputElementCity.property("value");
  
    console.log(inputValueDate);
    console.log(inputValueCity);
    
    console.log(sightings);
    // console.log(typeof inputValue);
    if (inputValueDate != "" && inputValueCity != ""){
        var filteredData = sightings.filter(
            sighting => 
                Date.parse(sighting.datetime) === Date.parse(inputValueDate) &&
                sighting.city.toLowerCase() === inputValueCity.toLowerCase()
            );
    } else if (inputValueDate == "") {
        var filteredData = sightings.filter(
            sighting => 
                sighting.city.toLowerCase() === inputValueCity.toLowerCase()
            );
    } else if (inputValueCity == "") {
        var filteredData = sightings.filter(
            sighting => 
                Date.parse(sighting.datetime) === Date.parse(inputValueDate) 
            );
    }
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