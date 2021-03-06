﻿========================================
FabianN's Re-Packed Minecraft Overviewer
﻿========================================
By Andrew Brown and contributors (see CONTRIBUTORS.rst).

http://github.com/brownan/Minecraft-Overviewer

Generates large resolution images of a Minecraft map.

In short, this program reads in Minecraft world files and renders very large
resolution images that can be viewed through a Google Maps interface. It
performs a similar function to the existing Minecraft Cartographer program but
with a slightly different goal in mind: to generate large resolution images
such that one can zoom in and see details.

See some examples here!
http://github.com/brownan/Minecraft-Overviewer/wiki/Map-examples

Further documentation may be found at
https://github.com/brownan/Minecraft-Overviewer/wiki/Documentation

Documentation for the add-ons to WorldGuard can be found in their respective directories under the web_assets directory.

To contact the developers and other users, go to the site at the top of this
README, or go to #overviewer on irc.freenode.net.

Features
========

* Renders large resolution images of your world, such that you can zoom in and
  see details

* Customizable textures! Pulls textures straight from your installed texture
  pack!

* Outputs a Google Map powered interface that is memory efficient, both in
  generating and viewing.

* Renders efficiently in parallel, using as many simultaneous processes as you
  want!

* Utilizes caching to speed up subsequent renderings of your world.

* Throw the output directory up on a web server to share your Minecraft world
  with everyone!

FabianN's Additions
-------------------

* Built in MapMarkers for Bukkit <http://forums.bukkit.org/threads/843> support. *Requires Setup*

* Built in ChatterCraft for Bukkit <http://forums.bukkit.org/threads/16448> support. Added thanks to helluvamatt. *Requires Setup*

* The player's skin used for the player's mapmarker. *Requires MapMarkers to be Setup*

* A list of currently online players which links you to the location of the player on the map. *Requires MapMarkers to be Setup*

* A timestamp of when the map was generated.

* Sundial, current server time with a day/night graphic. *Requires Setup*

* WorldGuard Region highlighting. *Requires Setup*

* Minecraft weather display (current and forcast). *Requires Setup*

Requirements
============
This program requires:

* Python 2.6 or 2.7 <http://python.org/download/>
* PIL (Python Imaging Library) <http://www.pythonware.com/products/pil/>
* Numpy <http://scipy.org/Download>
* Either the Minecraft client installed, or a terrain.png file. See the
  `Textures`_ section below.
* A C compiler.
* Bukkit's MapMarkers plugin <http://forums.bukkit.org/threads/mapmarkers-v0-2.843/>
* nbt.class.php by Justin Martian available at <http://thefrozenfire.com/2010/12/nbt-decoderencoder-for-php/>. Place in either the web_assets folder or in the web directory for the map, same location as index.html.
* WorldGuard Plugin <http://forums.bukkit.org/threads/sec-worldguard-5-0-alpha9-multi-world-fire-and-polygonal-cuboid-region-protection-with-blacklist.790/>

If you download a binary package, then some or all of these may not be required.

I develop and test this on Linux, but need help testing it on Windows and Mac.
If something doesn't work, let me know.

Using the Overviewer
====================

For a quick-start guide, see
https://github.com/brownan/Minecraft-Overviewer/wiki/Quick-Start-Guide

If you are upgrading from an older Overviewer to the new DTT code, see
https://github.com/brownan/Minecraft-Overviewer/wiki/DTT-Upgrade-Guide

Disclaimers
-----------
Before you dive into using this, just be aware that, for large maps, there is a
*lot* of data to parse through and process. If your world is very large, expect
the initial render to take at least an hour, possibly more. (Since Minecraft
maps are practically infinite, the maximum time this could take is also
infinite!)

If you press ctrl-C, it will stop. The next run will pick up where it left off.

Once your initial render is done, subsequent renderings will be MUCH faster due
to all the caching that happens behind the scenes. Just use the same output
directory and it will only update the tiles it needs to.

There are probably some other minor glitches along the way, hopefully they will
be fixed soon. See the `Bugs`_ section below.

Textures
--------
The Overviewer uses actual textures to render your world. However, I don't
include textures in the package. You will need to do one of two things before
you can use the Overviewer:

* Make sure the Minecraft client is installed. The Overviewer will find the
  installed minecraft.jar and extract the textures from it.

* Install a texture file yourself. This file is called "terrain.png" and is
  normally found in your minecraft.jar file (not "Minecraft.jar", the launcher,
  but rather the file that's downloaded by the launcher and installed into a
  hidden directory). You can also get this file from any of the third party
  texture packs out there.

Biome Tinting
-------------
With the Halloween update, biomes were added to Minecraft.  In order to get
biome-accurate tinting, the Overviewer can use biome data produced by the
Minecraft Biome Extractor tool.  This tool can be downloaded from:
http://www.minecraftforum.net/viewtopic.php?f=25&t=80902

If the "biomes" folder is present in the world directory, then the Overviewer
will use the biome data to tint grass and leaves automatically -- there is no
command line option to turn this feature on.  If this folder does not exist,
then the Overviewer will use a static tinting for grass and leaves.

MapMarker
---------
MapMarkers support has been integrated into Overviewer. For MapMarkers to work you need to have the MapMarkers Bukkit plugin installed which can be downloaded here: http://forums.bukkit.org/threads/843

Edit the MapMarker's config file to output the file to "*<LOCATIONOFMAP>/mapmarkers/markers.json*"

ChatterCraft
------------
ChatterCraft support has been intergrated into Overviewer. For ChatterCraft to work you need to have the ChatterCraft Bukkit plugin installed which can be downloaded here: http://forums.bukkit.org/threads/16448

Sundial
-------
Sundial displays the current time and a rotating image that reflects the sun/moon.

**Setup Requirements :**

* nbt.class.php needs to be placed in "*<LOCATIONOFOVERVIEWER>/web_assets*". You can download nbt.class.php from <http://thefrozenfire.com/2010/12/nbt-decoderencoder-for-php/>. Look for the link to his Subversion repository and nbt.class.php should be listed there.

* You will need to edit the file "*<LOCATIONOFOVERVIEWER>/web_assets/sundial/getServerTime.php*". Where it says "*<serverDIR>/level.dat*", replace that with the location of the level.dat file of your minecraft world.


WorldGuard2OverviewerRegion
---------------------------
WorldGuard displays regions defined in WorldGuard with an overlay.

**Setup Requirements :**

* You will need to edit the file "*<LOCATIONOFOVERVIEWER>/web_assets/wg_region/regions5.js.php*". Where it says "*<serverdir>\plugins\WorldGuard\worlds\<worldname>\regions.yml*", replace that with the location of the regions.yml file for WorldGuard.

MCWeather
---------
MCWeather displays current weather and the forcast with a count-down timer to when the next weather pattern will occure.

**Setup Requirements :**

* nbt.class.php needs to be placed in "*<LOCATIONOFOVERVIEWER>/web_assets*". You can download nbt.class.php from <http://thefrozenfire.com/2010/12/nbt-decoderencoder-for-php/>. Look for the link to his Subversion repository and nbt.class.php should be listed there.

* You will need to edit the file "*<LOCATIONOFOVERVIEWER>/web_assets/mcweather/getServerWeather.php*". Where it says "*<serverDIR>/level.dat*", replace that with the location of the level.dat file of your minecraft world.

Compiling the C Extension
------------------------- 
The C Extension for Overviewer is no longer optional.  In addition to
providing a higher quality image compositing function that looks better on
maps with lighting enabled, it now does the bulk of the rendering.

If you downloaded Overviewer as a binary package, this extension will already
be compiled for you.

If you have a C compiler and the Python development libraries set up, you can
compile this extension like this::

    python setup.py build

Note that you need the development headers for your version of Python installed,
look for a package named 'python-dev', 'python-devel' or similar. Also, some
Python distributions do not install "Imaging.h" and "ImPlatform.h" properly. If
you get errors complaining about them, you can get them from the PIL source, or
at <http://svn.effbot.org/public/tags/pil-1.1.7/libImaging/>. Just put them in
the same directory as "overviewer.py".

For more detailed instructions, check the wiki: 
https://github.com/brownan/Minecraft-Overviewer/wiki/Build-Instructions

Running
-------
To generate a set of Google Map tiles, use the overviewer.py script like this::

    python overviewer.py [OPTIONS] <World # / Name / Path to World> <Output Directory>

The output directory will be created if it doesn't exist. This will generate a
set of image tiles for your world in the directory you choose. When it's done,
you will find an index.html file in the same directory that you can use to view
it.


Options
-------

-h, --help
    Shows the list of options and exits

-p PROCS, --processes=PROCS
    Adding the "-p" option will utilize more cores during processing.  This
    can speed up rendering quite a bit. The default is set to the same
    number of cores in your computer, but you can adjust it.

    Example to run 5 worker processes in parallel::

        python overviewer.py -p 5 <Path to World> <Output Directory>

-d, --delete
    This option changes the mode of execution. No tiles are rendered, and
    instead, files are deleted.

    *Note*: Currently only the overviewer.dat file is deleted when you run with
    this option

--regionlist=regionlist
    Use this option to specify manually a list of regions to consider for
    updating. Without this option, every chunk in every region is checked for
    update and if necessary, re-rendered. If this option points to a file
    containing, 1 per line, the path to a region data file, then only those
    in the list will be considered for update.

    It's up to you to build such a list. On Linux or Mac, try using the "find"
    command. You could, for example, output all region files that are older than
    a certain date. Or perhaps you can incrementally update your map by passing
    in a subset of regions each time. It's up to you!

--rendermodes=MODE1[,MODE2,...]
    Use this option to specify which render mode to use, such as lighting or
    night. Use --list-rendermodes to get a list of available rendermodes, and
    a short description of each. If you provide more than one mode (separated
    by commas), Overviewer will render all of them at once, and provide a
    toggle on the resulting map to switch between them.

--list-rendermodes
    List the available render modes, and a short description of each.

--settings=PATH
    Use this option to load settings from a file. The format of this file is
    given below.


Settings
--------

You can optionally store settings in a file named settings.py (or really,
anything you want).  It is a regular python script, so you can use any python
functions or modules you want. To use a settings file, use the --settings
command line option.

For a sample settings file, look at 'sample.settings.py'. Note that this file
is not meant to be used directly, but instead it should be used as a
collection of examples to guide writing your own.

Here's a (possibly incomplete) list of available settings, which are available
in settings.py. Note that you can also set command-line options in a similar
way.

imgformat=FORMAT
    Set the output image format used for the tiles. The default is 'png',
    but 'jpg' is also supported.

zoom=ZOOM
    The Overviewer by default will detect how many zoom levels are required
    to show your entire map. This option sets it manually.

    *You do not normally need to set this option!*

    This is equivalent to setting the dimensions of the highest zoom level. It
    does not actually change how the map is rendered, but rather *how much of
    the map is rendered.* (Calling this option "zoom" may be a bit misleading,
    I know)
   
    To be precise, it sets the width and height of the highest zoom level, in
    tiles. A zoom level of z means the highest zoom level of your map will be
    2^z by 2^z tiles.

    This option map be useful if you have some outlier chunks causing your map
    to be too large, or you want to render a smaller portion of your map,
    instead of rendering everything.

    Remember that each additional zoom level adds 4 times as many tiles as
    the last. This can add up fast, zoom level 10 has over a million tiles.
    Tiles with no content will not be rendered, but they still take a small
    amount of time to process.

web_assets_hook
    This option lets you define a function to run after the web assets have
    been copied into the output directory, but before any tile rendering takes
    place. This is an ideal time to do any custom postprocessing for
    markers.js or other web assets.
    
    This function should accept one argument: a QuadtreeGen object.

web_assets_path
    This option lets you provide alternative web assets to use when
    rendering. The contents of this folder will be copied into the output folder
    during render, and will overwrite any default files already copied by
    Overviewer. See the web_assets folder included with Overviewer for the
    default assets.

textures_path
    This is like web_assets_path, but instead it provides an alternative texture
    source. Overviewer looks in here for terrain.png and other textures before
    it looks anywhere else.

Viewing the Results
-------------------
Within the output directory you will find two things: an index.html file, and a
directory hierarchy full of images. To view your world, simply open index.html
in a web browser. Internet access is required to load the Google Maps API
files, but you otherwise don't need anything else.

You can throw these files up to a web server to let others view your map. You
do *not* need a Google Maps API key (as was the case with older versions of the
API), so just copying the directory to your web server should suffice. You are,
however, bound by the Google Maps API terms of service.

http://code.google.com/apis/maps/terms.html

Crushing the Output Tiles
-------------------------
Image files taking too much disk space? Try using pngcrush. On Linux and
probably Mac, if you have pngcrush installed, this command will go and crush
all your images in the given destination. This took the total disk usage of the
render for my world from 85M to 67M.

::

    find /path/to/destination -name "*.png" -exec pngcrush {} {}.crush \; -exec mv {}.crush {} \;

Or if you prefer a more parallel solution, try something like this::

    find /path/to/destination -print0 | xargs -0 -n 1 -P <nr_procs> sh -c 'pngcrush $0 temp.$$ && mv temp.$$ $0'

If you're on Windows, I've gotten word that this command line snippet works
provided pngout is installed and on your path. Note that the % symbols will
need to be doubled up if this is in a batch file.

::

    FOR /R c:\path\to\tiles\folder %v IN (*.png) DO pngout %v /y

Bugs
====
This program has bugs. They are mostly minor things, I wouldn't have released a
completely useless program. However, there are a number of things that I want
to fix or improve.

For a current list of issues, visit
http://github.com/brownan/Minecraft-Overviewer/issues

Feel free to comment on issues, report new issues, and vote on issues that are
important to you, so I can prioritize accordingly.

An incomplete list of things I want to do soon is:

* Improve efficiency

* Some kind of graphical interface.


Changes by FabianN
------------------
This is just my personal configuration of Overviewer and I decided to share it, maybe make it easier for someone to host their own map with MapMarkers integration and many other great additions. My additions would not be possible without the work of others who created many of these components (I just put it all together). Here the pieces of code from others that I have intergrated with my package of Overviewer:

* The user's skin showing up as their icon on the map. Thanks to ethzero/Billiam for the Player-Avatar add-on. https://github.com/Billiam/Minecraft-Overviewer-Addons

* The Online Players list. Thanks to datLicht for the player list. http://forums.bukkit.org/threads/mapmarkers-v0-2.843/page-2#post-37817

* Sundial and server time. Thanks to Sunkid for the sundial. https://github.com/sunkid/minecraft-sundial

* WorldGuard overlay. Thanks to Pironic for WorldGuard2OverviewerRegion. https://github.com/pironic/Minecraft-Overviewer-Addons/tree/master/WG2OvR

* MCWeather. Thanks to Pironic for MCWeather. https://github.com/pironic/Minecraft-Overviewer-Addons/tree/master/mcweather
