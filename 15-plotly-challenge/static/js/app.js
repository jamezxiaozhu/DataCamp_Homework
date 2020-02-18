function buildMetadata(sample) {

  // @TODO: Complete the following function that builds the metadata panel

  // Use `d3.json` to fetch the metadata for a sample
  d3.json("/metadata/"+sample).then(function(data){
    // Use d3 to select the panel with id of `#sample-metadata`
    // Use `.html("") to clear any existing metadata
    d3.select("#sample-metadata").html("")
    // Use `Object.entries` to add each key and value pair to the panel
    // Hint: Inside the loop, you will need to use d3 to append new
    // tags for each key-value in the metadata.
    Object.entries(data).forEach(([key, value]) => {
      var cell = d3.select("#sample-metadata").append("p");
      cell.text(key + ": " +value);
    });


    // BONUS: Build the Gauge Chart
    function buildGauge(dataInput){
      var data = [
        {
          domain: { x: [0, 1], y: [0, 1] },
          value: dataInput,
          title: { text: "Scrubs per Week" },
          type: "indicator",
          mode: "gauge+number"
        }
      ];
      
      var layout = { width: 600, height: 500, margin: { t: 0, b: 0 } };
      Plotly.newPlot('gauge', data, layout);

    }
    buildGauge(sample.WFREQ);
    
    
  }


  )
    
}

function buildCharts(sample) {

  // @TODO: Use `d3.json` to fetch the sample data for the plots
  d3.json("/samples/"+sample).then(function(sampleInput){
    // @TODO: Build a Bubble Chart using the sample data
    var trace1 = {
      x: sampleInput.otu_ids,
      y: sampleInput.sample_values,
      mode: 'markers',
      marker: {
        size: sampleInput.sample_values,
        color: sampleInput.otu_ids
      },
      text:sampleInput.otu_labels
    };
    
    var dataBubble = [trace1];
    
    // var layoutBubble = {
    //   title: 'Marker Size',
    //   showlegend: false,
    //   height: 600,
    //   width: 600
    // };
    
    Plotly.newPlot('bubble', dataBubble);
    // @TODO: Build a Pie Chart
    var data = [{
      values: sampleInput.sample_values.slice(0,11),
      labels: sampleInput.otu_ids.slice(0,11),
      hoverinfo:sampleInput.otu_labels.slice(0,11),
      type: 'pie'
    }];
    
    // var layout = {
    //   height: 400,
    //   width: 500
    // };
    
    Plotly.newPlot('pie', data);
    // HINT: You will need to use slice() to grab the top 10 sample_values,
    // otu_ids, and labels (10 each).
  }
  )
}

function init() {
  // Grab a reference to the dropdown select element
  var selector = d3.select("#selDataset");

  // Use the list of sample names to populate the select options
  d3.json("/names").then((sampleNames) => {
    sampleNames.forEach((sample) => {
      selector
        .append("option")
        .text(sample)
        .property("value", sample);
    });

    // Use the first sample from the list to build the initial plots
    const firstSample = sampleNames[0];
    buildCharts(firstSample);
    buildMetadata(firstSample);
  });
}

function optionChanged(newSample) {
  // Fetch new data each time a new sample is selected
  buildCharts(newSample);
  buildMetadata(newSample);
}

// Initialize the dashboard
init();
