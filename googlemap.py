#    This file is part of the Minecraft Overviewer.
#
#    Minecraft Overviewer is free software: you can redistribute it and/or
#    modify it under the terms of the GNU General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or (at
#    your option) any later version.
#
#    Minecraft Overviewer is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General
#    Public License for more details.
#
#    You should have received a copy of the GNU General Public License along
#    with the Overviewer.  If not, see <http://www.gnu.org/licenses/>.

import os
import os.path
import stat
import cPickle
import Image
import shutil
from time import strftime, gmtime, localtime
import json

import util

"""
This module has routines related to generating a Google Maps-based
interface out of a set of tiles.

"""

def mirror_dir(src, dst, entities=None):
    '''copies all of the entities from src to dst'''
    if not os.path.exists(dst):
        os.mkdir(dst)
    if entities and type(entities) != list: raise Exception("Expected a list, got a %r instead" % type(entities))
    
    # files which are problematic and should not be copied
    # usually, generated by the OS
    skip_files = ['Thumbs.db', '.DS_Store']
    
    for entry in os.listdir(src):
        if entry in skip_files:
            continue
        if entities and entry not in entities:
            continue
        
        if os.path.isdir(os.path.join(src,entry)):
            mirror_dir(os.path.join(src, entry), os.path.join(dst, entry))
        elif os.path.isfile(os.path.join(src,entry)):
            try:
                shutil.copy(os.path.join(src, entry), os.path.join(dst, entry))
            except IOError:
                # maybe permission problems?
                os.chmod(os.path.join(src, entry), stat.S_IRUSR)
                os.chmod(os.path.join(dst, entry), stat.S_IWUSR)
                shutil.copy(os.path.join(src, entry), os.path.join(dst, entry))
                # if this stills throws an error, let it propagate up

class MapGen(object):
    def __init__(self, quadtrees, skipjs=False, web_assets_hook=None):
        """Generates a Google Maps interface for the given list of
        quadtrees. All of the quadtrees must have the same destdir,
        image format, and world. 
        Note:tiledir for each quadtree should be unique. By default the tiledir is determined by the rendermode"""
        
        self.skipjs = skipjs
        self.web_assets_hook = web_assets_hook
        
        if not len(quadtrees) > 0:
            raise ValueError("there must be at least one quadtree to work on")
        
        self.destdir = quadtrees[0].destdir
        self.imgformat = quadtrees[0].imgformat
        self.world = quadtrees[0].world
        self.p = quadtrees[0].p
        for i in quadtrees:
            if i.destdir != self.destdir or i.imgformat != self.imgformat or i.world != self.world:
                raise ValueError("all the given quadtrees must have the same destdir")
        
        self.quadtrees = quadtrees
        
    def go(self, procs):
        """Writes out config.js, marker.js, and region.js
        Copies web assets into the destdir"""
        zoomlevel = self.p
        imgformat = self.imgformat
        configpath = os.path.join(util.get_program_path(), "config.js")

        config = open(configpath, 'r').read()
        config = config.replace(
                "{maxzoom}", str(zoomlevel))
        config = config.replace(
                "{imgformat}", str(imgformat))
        
        config = config.replace("{spawn_coords}",
                                json.dumps(list(self.world.spawn)))
        
        # create generated map type data, from given quadtrees
        maptypedata = map(lambda q: {'label' : q.rendermode.capitalize(),
                                     'path' : q.tiledir}, self.quadtrees)
        config = config.replace("{maptypedata}", json.dumps(maptypedata))
        
        with open(os.path.join(self.destdir, "config.js"), 'w') as output:
            output.write(config)

        # Write a blank image
        for quadtree in self.quadtrees:
            blank = Image.new("RGBA", (1,1))
            tileDir = os.path.join(self.destdir, quadtree.tiledir)
            if not os.path.exists(tileDir): os.mkdir(tileDir)
            blank.save(os.path.join(tileDir, "blank."+self.imgformat))

        # copy web assets into destdir:
        mirror_dir(os.path.join(util.get_program_path(), "web_assets"), self.destdir)

        # Add time in index.html
        indexpath = os.path.join(self.destdir, "index.html")

        index = open(indexpath, 'r').read()
        index = index.replace(
                "{time}", str(strftime("%a, %d %b %Y %I:%M:%S %S %Z", localtime())))

        with open(os.path.join(self.destdir, "index.html"), 'w') as output:
            output.write(index)

        if self.skipjs:
            if self.web_assets_hook:
                self.web_assets_hook(self)
            return


    def finalize(self):
        if self.skipjs:
            return

        # since we will only discover PointsOfInterest in chunks that need to be 
        # [re]rendered, POIs like signs in unchanged chunks will not be listed
        # in self.world.POI.  To make sure we don't remove these from markers.js
        # we need to merge self.world.POI with the persistant data in world.PersistentData

        self.world.POI += filter(lambda x: x['type'] != 'spawn', self.world.persistentData['POI'])

        # write out the default marker table
        with open(os.path.join(self.destdir, "markers.js"), 'w') as output:
            output.write("var markerData=[\n")
            for marker in self.world.POI:
                output.write(json.dumps(marker))
                if marker != self.world.POI[-1]:
                    output.write(",")
                output.write("\n")
            output.write("]\n")
        
        # save persistent data
        self.world.persistentData['POI'] = self.world.POI
        with open(self.world.pickleFile,"wb") as f:
            cPickle.dump(self.world.persistentData,f)

        # write out the default (empty, but documented) region table
        with open(os.path.join(self.destdir, "regions.js"), 'w') as output:
            output.write('var regionData=[\n')
            output.write('  // {"color": "#FFAA00", "opacity": 0.5, "closed": true, "path": [\n')
            output.write('  //   {"x": 0, "y": 0, "z": 0},\n')
            output.write('  //   {"x": 0, "y": 10, "z": 0},\n')
            output.write('  //   {"x": 0, "y": 0, "z": 10}\n')
            output.write('  // ]},\n')
            output.write('];')
        
