
var data = 'data.json'
var world_countries = 'world_countries.json'
var dataset = 0

var requests = [d3.json(world_countries), d3.json(data)]
var format = d3.format(",");

Promise.all(requests).then(function(response) {
  dataset = response
  data = response[0]
  var gdp_forecast = response[1]

  // deinfe margin, h and w of svg for the map
  var svg = d3.select("svg"),
      margin = {top:0 , right: 0, bottom: 0, left: 0},
      height = 550;
      width = 800;

  // make the svg for the map
  var svg = d3.select("body")
      .append("svg")
      .attr("width", width)
      .attr("height", height)
      .append('g')
      .attr('class', 'map')
      .attr('transform', 'translate(0, -0)');

    // make title of map
    svg.append('text')
      .attr('class', 'title')
      .attr('x', width / 2)
      .attr('y', 20)
      .attr('text-anchor', 'middle')
      .text('Map of the world with GDP forecast ')

  // make map (function called) when page is loaded and display forecast for year 2020
  map(svg, data, gdp_forecast, '2020', height, width, margin)

  // deinfe margin, h and w of svg for scatterplot
  var svg2 = d3.select("svg"),
      margin2 = {top: 30, right: 30, bottom: 30, left: 50},
      h = 400,
      w = 750;

  // make x_scale
  var x_scale = d3.scaleLinear()
      .domain([2008.7, 2020])
      .range([margin2.left, w - margin2.right]);

  // make y_scale
  var y_scale = d3.scaleLinear()
    .domain([-7, 11.1])
    .range([h - margin2.top, margin2.bottom]);

  // Create SVG element for scatterplot
  var svg2 = d3.select("body")
    .append("svg")
    .attr("width", w)
    .attr("height", h)

  // On click in dropdown button, update map (colors) with new data
  d3.selectAll(".m")
    .on("click", function() {

    // index is the year clicked on by the user
    var index = this.getAttribute("value");
    index = index.toString();
    console.log(index);

    // give index to the map function, so it shows the right year
    map(svg, data, gdp_forecast, index, height, width, margin);

    // if a specific country is clicked on, the scatterplot with the gdp forecasts over the years appears
    d3.selectAll("path")
      .on("click", function(d) {
      console.log(d)

      // make scatterplot, add titles and add axis for specific country
      make_titles(svg2, h, w, margin2, d.properties['name'])
      make_scatter(gdp_forecast, d.id, svg2, x_scale, y_scale, margin2, h, w)
      make_axis(svg2, x_scale, y_scale, h, w, margin2)

      })
    })

    // if a specific country is clicked on, the scatterplot with the gdp forecasts
    // over the years appears (this function is needed because otherwise when there hasn't been
    // clicked on the dropdown button yet, the scatterplot would'nt appear)
  d3.selectAll("path")
    .on("click", function(d) {

    // make scatterplot, add titles and add axis for specific country
    make_titles(svg2, h, w, margin2, d.properties['name'])
    make_scatter(gdp_forecast, d.id, svg2, x_scale, y_scale, margin2, h, w)
    make_axis(svg2, x_scale, y_scale, h, w, margin2)

    })


}).catch(function(e){
  throw(e);
})


function map(svg, data, gdp_forecast, index, height, width, margin){
  // this function draws the map

    // Set tooltips
    var tip = d3.tip()
              .attr('class', 'd3-tip')
              .offset([-10, 0])
              .html(function(d) {
                return "<strong>Country: </strong><span class='details'>" + d.properties.name + "<br></span>" + "<strong>Forecast gdp: </strong><span class='details'>"  + format(d.gdp) + "<br></span>" + "<strong>Year: </strong><span class='details'>" + index + "<br></span>";
              })

    // make color range for the different percentages of gdp forecasts
    var color = d3.scaleThreshold()
      .domain([-5,-3,-1,1,3,5,7,9,11])
      .range(["rgb(222,235,247)", "rgb(198,219,239)", "rgb(158,202,225)", "rgb(107,174,214)", "rgb(66,146,198)","rgb(33,113,181)","rgb(8,81,156)","rgb(8,48,107)","rgb(3,19,43)"])


    var path = d3.geoPath();

    var projection = d3.geoMercator()
                     .scale(130)
                     .translate([width / 2, (height) / 1.5]);

    var path = d3.geoPath().projection(projection);

    svg.call(tip);

    // find for the year the gdp forecast values of all countries in dataset to display on the map
    gdp_byID = {}
    gdp_forecast.forEach(function(d) { gdp_byID[d['location']] = +d[index]; });
    data.features.forEach(function(d) { d.gdp = gdp_byID[d.id] });

    // start drawing the map with the data
    svg.append("g")
        .attr("class", "countries")
        .attr('transform', 'translate(0, 32)')
      .selectAll("path")
        .data(data.features)
      .enter().append("path")
        .attr("d", path)
        // determine gdp color per country
        .style("fill", function(d) { return color(gdp_byID[d.id])})
        .style('stroke', 'white')
        .style('stroke-width', 1.5)
        .style("opacity",1)
        // tooltips
        .style("stroke","white")
        .style('stroke-width', 0.3)
        .on('mouseover',function(d){
              tip.show(d);
            d3.select(this)
                    .style("opacity", 1)
                    .style("stroke","white")
                    .style("stroke-width",3);
                })
                .on('mouseout', function(d){
                  tip.hide(d);

                  d3.select(this)
                    .style("opacity", 1)
                    .style("stroke","white")
                    .style("stroke-width",0.3);
                });

}

function make_scatter(data_all, id, svg, x_scale, y_scale, margin, h, w) {

  // remove scatter dots from svg file
  svg.selectAll("circle")
    .remove()

  var data = 0

  // if ID of country clicked on is in the datafile, collect all data of that country
  for (i = 0; i < data_all.length ; i++ ){
    if (data_all[i]['location'] == id){
      var data = data_all[i]
      console.log(data_all[i]['location'])
    }
}
    // if the ID of country clicked on is in dataset, draw scatterplot with values
    if (data != 0){

    // add tip element for each scatterdot
    var tip = d3.tip()
      .attr('class', 'd3-tip')
      .offset([-10, 0])
      .html(function(d, i) {
        return d['year'] + ": " + d['value'];
      })

    // make a dictionary with the values asigned to the right year
    dict_country_year = {}
    list_values = []
    for(i = 2009; i <= 2020; i++){
      dict_country_year['year'] = i.toString()
      dict_country_year['value'] = data[i]
      list_values.push(dict_country_year)
      dict_country_year = {}
    }

    // call tip in svg
    svg.call(tip);

    // determine color range
    var color = d3.scaleThreshold()
    .domain([-5,-3,-1,1,3,5,7,9,11])
    .range(["rgb(222,235,247)", "rgb(198,219,239)", "rgb(158,202,225)", "rgb(107,174,214)", "rgb(66,146,198)","rgb(33,113,181)","rgb(8,81,156)","rgb(8,48,107)","rgb(3,19,43)"])

    // make scatter dots in scatterplot
    svg.selectAll("circle")
      .data(list_values)
      .enter()
      .append("circle")
      .attr("cx", function(d) {
        return x_scale(parseInt(d['year']));
      })
      .attr("cy", function(d) {
        return y_scale(parseFloat(d['value']));
      })
      .attr("r", 5)
      // determine color per year
      .attr("fill", function(d) { return color(d['value'])
    })
      // // show gdp forecast per dot
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

    // else there was no data available for the clicked country, add title to scatterplot with
    // 'no data available'
    else {
      make_titles(svg, h, w, margin, 'No data available')
      svg.selectAll('circles')
        .remove()
    }

}

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

function make_titles(svg, h, w, margin, name){

    // remove titles from previous scatterplot
    svg.selectAll('text')
      .attr('class', 'title')
      .remove()

    // add scatterplot title
    svg.append('text')
      .attr('class', 'title')
      .attr('x', w / 2)
      .attr('y', 40)
      .attr('text-anchor', 'middle')
      .text(name)

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
      .attr('y', 20)
      .attr("transform", "rotate(-90)")
      .attr('text-anchor', 'middle')
      .text('GDP forecast in %')

}
