//hogeeeeeeeeeee

var morph;
var simil;
var node;

$('#my-select').multiSelect()

$(function() {
  var egm = egrid.core.egm()
    .size([$('#display-wrapper').width() - 15, 600]);
  var selection = d3.select('#display');
  var selection2 = d3.select('#cloud');

  d3.json('data/pen30/data.json', function(data) {
    var graph = egrid.core.graph.adjacencyList();
    data.nodes.forEach(function(node) {
      graph.addVertex(node);
    });
    data.links.forEach(function(link) {
      graph.addEdge(link.source, link.target);
    });

    selection
      .datum(graph)
      .call(egm.css())
      .call(egm)
      .call(egm.center());

  });

  d3.csv("morphological.php", function(data) {
	  morph = data;
	  //	  console.log(morph);
      }
  );

  d3.select('#search-form')
    .on('submit', function() {
      var word = d3.select('#search-word').node().value;
      var url = 'data/sample.json?word=' + word;

      d3.csv("writetext.php?word=" + word, function(data) {
	      simil = data;
	      //	      console.log(simil);
	      for (var j=0; j<=351 ; j++){
		  morph[j].similality = 0;
	      }
	      for (var i=0 ; i<=simil.length-1 ; i++){
		  if (simil[i].similality == "nan"){
		      simil[i].similality = 0;
		  }
		  for (var j=0; j<=351 ; j++){
		      if (simil[i].word ==  morph[j].word0){
			  if (simil[i].similality > morph[j].similality){
			      morph[j].similality = simil[i].similality;
			  }
		      }
		      if (simil[i].word ==  morph[j].word1){
			  if (simil[i].similality > morph[j].similality){
			      morph[j].similality = simil[i].similality;
			  }
		      }		  
		      if (simil[i].word ==  morph[j].word2){
			  if (simil[i].similality > morph[j].similality){
			      morph[j].similality = simil[i].similality;
			  }
		      }
		      if (simil[i].word ==  morph[j].word3){
			  if (simil[i].similality > morph[j].similality){
			      morph[j].similality = simil[i].similality;
			  }
		      }
		      if (simil[i].word ==  morph[j].word4){
			  if (simil[i].similality > morph[j].similality){
			      morph[j].similality = simil[i].similality;
			  }
		      }
		      if (simil[i].word ==  morph[j].word5){
			  if (simil[i].similality > morph[j].similality){
			      morph[j].similality = simil[i].similality;
			  }
		      }
                      if (simil[i].word ==  morph[j].word6){
                          if (simil[i].similality > morph[j].similality){
                              morph[j].similality = simil[i].similality;
                          }
                      }
                      if (simil[i].word ==  morph[j].word7){
                          if (simil[i].similality > morph[j].similality){
                              morph[j].similality = simil[i].similality;
                          }
                      }
                      if (simil[i].word ==  morph[j].word8){
                          if (simil[i].similality > morph[j].similality){
                              morph[j].similality = simil[i].similality;
                          }
                      }
		  }
	      };
	      node =  d3.select("#display").select("g.contents").select("g.vertices").selectAll("g.vertex");
	      //	      console.log(node);
	      console.log(morph);
	      var j = 0;
	      node[0].forEach(function(d){
		      d.style.opacity = morph[j].similality;
		      j= j +1;

		      /*
		      for (var j=0; j<=351 ; j++){
			  //			  if (d.textContent ==  morph[j].sentence){
			      d.style.opacity = morph[j].similality;
			      //			  }
		      }
		      */
		  }
	      );
	  }
	  );
      
      d3.json(url, function(result) {
	      var formText = d3.select("#word-form input").node;
	      var graph  =selection.datum();
	      var sizeScale = d3.scale.linear()
		  .domain(d3.extent(graph.vertices(), function(u) {
			      return result[graph.get(u).text];
			  }))
		  .range([1, 3]);
	      egm.vertexScale(function(node) {
		      return sizeScale(result[node.text]);
		  });
	      
	      selection.call(egm);
	  });
      
      d3.event.preventDefault();
    }
  );

  d3.select(window)
    .on('resize', function() {
      selection
        .call(egm.resize($('#display-wrapper').width(), 600));
    });
});
