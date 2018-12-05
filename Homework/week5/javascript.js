
window.onload = function() {

  var consConf = "http://stats.oecd.org/SDMX-JSON/data/HH_DASH/FRA+DEU+KOR+NLD+PRT+GBR.COCONF.A/all?startTime=2007&endTime=2015"

  var requests = d3.json(consConf);

  // var hallo = transformResponse(requests)

  var dataset = 0
  Promise.resolve(requests).then(function(response) {
    dataset = response
    var data = transformResponse(response)

    // deinfe margin, h and w of svg
    var svg = d3.select("svg"),
        margin = {top: 30, right: 30, bottom: 30, left: 50},
        h = 500,
        w = 800;

    // make x_scale
    var x_scale = d3.scaleLinear()
        .domain([2007, 2015])
        .range([margin.left, w - margin.right]);

    // make y_scale
    var y_scale = d3.scaleLinear()
      .domain([97, 102.5])
      .range([h - margin.top, margin.bottom]);

    // Create SVG element
    var svg = d3.select("body")
      .append("svg")
      .attr("width", w)
      .attr("height", h)

    // make axis, scatterplot and add titles
    make_axis(svg, x_scale, y_scale, h, w, margin)
    make_scatter(data, svg, x_scale,y_scale, h, w, margin)
    make_titles(svg, h, w, margin)

    //On click, update with new data
    d3.selectAll(".m")
      .on("click", function() {
      var index = this.getAttribute("value");
      var data_list = [];

      // define all if button all is pushed
      var index_begin = 0;

      // if index = 7, all countries are shown so data_list = data
      if (index == 7){
        data_list = data
        make_scatter(data_list, svg, x_scale, y_scale, h, w, margin)
      }

      // else find specific data for each country and put in data_list
      else {
        index_begin = (index - 1) * 9

      // put data of specific country to data_list
      for (i = index_begin; i <  index * 9 ; i++){
        data_list.push(data[i])
      }

      // call scatter-plot with new data of 1 specific country
      make_scatter(data_list, svg, x_scale, y_scale, h, w, margin)
    }
    })

  }).catch(function(e){
    throw(e);
  });

  // make axis
  function make_axis(svg, x_scale, y_scale, h, w, margin) {

    var xAxis = d3.axisBottom()
      .scale(x_scale)
      .tickFormat(d3.format(".0f"));

    var yAxis = d3.axisLeft()
      .scale(y_scale)

    // append group and insert axis
    var gX = svg.append("g")
      .attr("transform", "translate(" + 0 + "," +
          (h - margin.top) + ")")
      .call(xAxis)

      // append group and insert axis
    var gY = svg.append("g")
      .attr("transform", "translate(" + margin.left + "," +
          0 + ")")
      .call(yAxis);

  }

function make_scatter(data, svg, x_scale, y_scale, h, w, margin) {

    // remove scatter dots from svg file
    svg.selectAll("circle")
      .remove()

    // make tip for interactivity feature
    var tip = d3.tip()
      .attr('class', 'd3-tip')
      .offset([-10, 0])
      .html(function(d, i) {
        return d['Country'] + ": " + d['datapoint'];
      })

    // call tip in svg
    svg.call(tip);

    // make scatter dots in scatterplot
    svg.selectAll("circle")
      .data(data)
      .enter()
      .append("circle")
      .attr("cx", function(d) {
        return x_scale(parseInt(d['time']));
      })
      .attr("cy", function(d) {
        return y_scale(parseFloat(d['datapoint']));
      })
      .attr("r", 5)
      // determine color per country
      .attr("fill", function(d) {
        if (d['Country'] == 'France') {
          return 'blue' }
        if (d['Country'] == 'Netherlands') {
          return 'red' }
        if (d['Country'] == 'Portugal') {
          return 'GoldenRod ' }
        if (d['Country'] == 'Germany') {
            return 'green' }
        if (d['Country'] == 'United Kingdom') {
            return 'Indigo' }
        if (d['Country'] == 'Korea') {
            return 'DarkOrchid' }
      })
      // show consumer confidence per dot
      .on('mouseover', tip.show)
      .on('mousover', function () {
        d3.select(this)
        .transition()
        .duration(500)
        .attr('r',10)
        .attr('stroke-width',3)
      })
      .on('mouseout', tip.hide)
      .on('mouseout', function (d) {
        tip.hide(d)
        d3.select(this)
          .transition()
          .duration(500)
          .attr('r',5)
          .attr('stroke-width',1)
      })
}
  function make_titles(svg, h, w, margin){

      // add title
      svg.append('text')
        .attr('class', 'title')
        .attr('x', w / 2)
        .attr('y', 40)
        .attr('text-anchor', 'middle')
        .text('Consumer confidence over the years')

      // add x-as title
      svg.append('text')
        .attr('class', 'title')
        .attr('x', w - 100)
        .attr('y', h - 2)
        .attr('text-anchor', 'middle')
        .text('Years')

      // add y-as title
      svg.append('text')
        .attr('class', 'title')
        .attr('x', -100)
        .attr('y', 15)
        .attr("transform", "rotate(-90)")
        .attr('text-anchor', 'middle')
        .text('Consumer confidence')

}



    function transformResponse(data){

        // access data property of the response
        let dataHere = data.dataSets[0].series;

        // access variables in the response and save length for later
        let series = data.structure.dimensions.series;
        let seriesLength = series.length;

        // set up array of variables and array of lengths
        let varArray = [];
        let lenArray = [];

        series.forEach(function(serie){
            varArray.push(serie);
            lenArray.push(serie.values.length);
        });

        // get the time periods in the dataset
        let observation = data.structure.dimensions.observation[0];

        // add time periods to the variables, but since it's not included in the
        // 0:0:0 format it's not included in the array of lengths
        varArray.push(observation);

        // create array with all possible combinations of the 0:0:0 format
        let strings = Object.keys(dataHere);

        // set up output array, an array of objects, each containing a single datapoint
        // and the descriptors for that datapoint
        let dataArray = [];

        // for each string that we created
        strings.forEach(function(string){
            // for each observation and its index
            observation.values.forEach(function(obs, index){
                let data = dataHere[string].observations[index];
                if (data != undefined){

                    // set up temporary object
                    let tempObj = {};

                    let tempString = string.split(":").slice(0, -1);
                    tempString.forEach(function(s, indexi){
                        tempObj[varArray[indexi].name] = varArray[indexi].values[s].name;
                    });

                    // every datapoint has a time and ofcourse a datapoint
                    tempObj["time"] = obs.name;
                    tempObj["datapoint"] = data[0];
                    dataArray.push(tempObj);
                }
            });
        });

        // return the finished product!
        return dataArray;
    }

  };
