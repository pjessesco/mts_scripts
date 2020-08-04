import os
import sys
import subprocess
import glob

class Scene:
    def __init__(self, path, xml, name):
        self.path = path
        self.xml = xml
        self.scene_name = name
        

if __name__ == '__main__':

    scene_path = "path/to/scene/directory"
    scene_name_list = ["spaceship", "coffee", "conference", "veach-door", "staircase", "veach-bidir"]
    mitsuba_path = os.path.abspath("path/to/executable")

    scene_list = []


    for scene_name in scene_name_list:
        scene_xml_list = glob.glob(os.path.join(scene_path, scene_name, "mts2_*.xml"))
        
        for scene_xml in scene_xml_list:
            scene_list.append(Scene(os.path.join(scene_path, scene_name), os.path.basename(scene_xml), scene_name))

    scene_list.sort(key = lambda object:object.xml)
    scene_list.sort(key = lambda object:object.path)

    variant = ["scalar_rgb","packet_rgb"]


    for v in variant:

        for s in scene_list:

            executable = os.path.join(mitsuba_path, "mitsuba")
            var = "-m "+v

            scene = os.path.join(s.path, s.xml)

            output_name = s.scene_name+"_"+v+"_"+s.xml.split(".")[0]
            output = "-o "+output_name

            command = executable + " " + scene + " " + var + " " + output


            # print(command)
            os.system(command)
            print()
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("===========================================================")
            print()
