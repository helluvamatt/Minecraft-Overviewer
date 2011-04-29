var playerMarkers = null;
var warpMarkers = [];
var PlayerNames = null;
var PlayerCount = 0;

function deletePlayerMarkers() {
  if (playerMarkers) {
    for (i in playerMarkers) {
      playerMarkers[i].setMap(null);
    }
    playerMarkers = null;
	PlayerNames = null;
	PlayerCount = 0;
  }
}

setInterval(loadPlayerMarkers, 1000 * 5);
setTimeout(loadPlayerMarkers, 1000);

function preparePlayerMarker(marker,item) {
	var c = '<div class="infoWindow" style="width: 240px;" align="center"><img src="player_list/head.php?player=' + item.msg + '&usage=info"><font style="font-family:Arial; font-size:20px;"><b>' + item.msg + '</b></font></div>';
	var infowindow = new google.maps.InfoWindow({content: c});
	google.maps.event.addListener(marker, 'click', function() {
		infowindow.open(map,marker);
	});
}

function loadPlayerMarkers() {
    $.getJSON('mapmarkers/markers.json', function(data) {
        deletePlayerMarkers();
        playerMarkers = [];
		PlayerNames = [];
		PlayerCount = 0;

        for (i in data) {
            var item = data[i];
            var converted = overviewer.util.fromWorldToLatLng(item.x, item.y, item.z);
			
			var perPixel = 1.0 / (overviewerConfig.CONST.tileSize * Math.pow(2, overviewerConfig.map.maxZoom));

			var lng = 0.5 - (1.0 / Math.pow(2, overviewerConfig.map.maxZoom + 1));
			var lat = 0.5;
					
			lng += 12 * item.x * perPixel;
			lat -= 6 * item.x * perPixel;
					
			lng += 12 * item.z * perPixel;
			lat += 6 * item.z * perPixel;
					
			lat += 12 * (128 - item.y) * perPixel;

			lng += 12 * perPixel;
			lat += 18 * perPixel;


			PlayerNames.push('<!-- ' + item.msg.toLowerCase() + ' -->&nbsp;<a onclick="overviewer.map.panTo(new google.maps.LatLng('+lat+', '+lng+'));"><img src="player_list/head.php?player=' + item.msg + '&usage=list" border="0" /></a>&nbsp;' + item.msg + '<br /> ');
			PlayerCount++;
            
			var marker = new google.maps.Marker({
                    position: converted,
                    map: overviewer.map,
                    title: item.msg,
                    icon: 'player_list/head.php?player=' + item.msg + '&usage=marker'
            });
			playerMarkers.push(marker);
			preparePlayerMarker(marker, item);
         }
		
		$("#Players").empty();

		if(PlayerCount == 0)
		{
			$("#Players").html('&nbsp;<font color="lightgreen">' + PlayerCount + '</font> players online');
		}
		else
		{
			PlayerNames.sort();
			
			$("#Players").html('&nbsp;<font color="lightgreen">' + PlayerCount + '</font> players online:<br /><br />' + PlayerNames.join(" "));
		}
	});
}

loadPlayerMarkers();
