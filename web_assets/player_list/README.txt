Addon to MapMarkers by datLicht

- Online Player List
- Markers are heads
- Info Window shows full avatar


INSTALLATION:

1. Copy the full content of MMLicht.rar to your overviewer web dir
2. Edit your index.html:

		add (below line: <div id="mcmap" style="width:100%; height:100%"></div>) :
		
		  <div id="playerList" style="position:absolute; background-image:url(./listbg.png); top:55px; right:20px; width:150px; height:*;border:solid;border-color:#FFFFFF;border-width:1px;color:#FFFFFF;font-family:Arial;">
			<strong>
				<div align="center" style="font-size:80%; position:relative; top:5px;">&nbsp;Online List&nbsp;</div>
				<hr style="color:#FFFFFF; background:#FFFFFF; heigth:1px;" />
				<div style="font-size:80%; left:10px; bottom:10px; top:5px" id="Spieler"></div>
			</strong>
		  </div>


		add (below line: <script type="text/javascript" src="http://code.jquery.com/jquery-1.4.3.min.js"></script>) :
		  <script type="text/javascript" src="player_markers.js"></script>

3. enjoy your MapMarkers



As seen on http://www.k9-kommando.de/mm
(without Chat Window)