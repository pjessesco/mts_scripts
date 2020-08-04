from xml.etree.ElementTree import parse, Element, dump
from xml.etree import ElementTree
import random
import math
from datetime import datetime
import os
import glob


if __name__ == '__main__':


    SPP = '50'
    MAXDEPTH = ['1','2','3','4','5','6','7','8','9','10',]
    SCENE_LIST = ['coffee', 'conference', 'spaceship', 'staircase', 'veach-bidir', 'veach-door']

    for scene in SCENE_LIST:
        scenes_path = os.path.join("path/to/scene/directory", scene)

        xml_list = glob.glob(os.path.join(scenes_path, "*.xml"))

        for xml in xml_list:

            for depth in MAXDEPTH:

                filename_ext = os.path.basename(xml)
                filename = filename_ext.partition('.')[0]

                if xml.find("modified") != -1:
                    print("ERROR : tried to modify modified scene, exit")
                    exit(-1)

                tree = parse(xml)
                root = tree.getroot()

                # Fix spp
                spp = root.find("sensor").find("sampler").find("integer")
                spp.set('value', SPP)

                # Fix max depth
                # maxdepth = root.find("integrator").find("integer")
                # maxdepth.set('value', depth)

                modified_filename = "modified_"+filename + "_"+SPP+"_"+depth+".xml"

                modified_path = os.path.join(scenes_path, modified_filename)

                tree.write(modified_path)
