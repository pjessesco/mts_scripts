import os
import sys
import subprocess


class Scene:
    def __init__(self, path, xml, name):
        self.path = path
        self.xml = xml
        self.scene_name = name
        
scene_path = "path/to/scene/directory"

if __name__ == '__main__':


    scene_list = [  
                    Scene(os.path.join(scene_path, "coffee"), "mts1_path.xml", "coffee"),
                    Scene(os.path.join(scene_path, "coffee"), "mts1_gpt.xml", "coffee"),

                    Scene(os.path.join(scene_path, "conference"), "mts1_path.xml", "conference"),
                    Scene(os.path.join(scene_path, "conference"), "mts1_gpt.xml", "conference"),
                    
                    Scene(os.path.join(scene_path, "spaceship"), "mts1_path.xml", "spaceship"),
                    Scene(os.path.join(scene_path, "spaceship"), "mts1_gpt.xml", "spaceship"),
                    
                    Scene(os.path.join(scene_path, "staircase"), "mts1_path.xml", "staircase"),
                    Scene(os.path.join(scene_path, "staircase"), "mts1_gpt.xml", "staircase"),
                    
                    Scene(os.path.join(scene_path, "veach-bidir"), "mts1_path.xml", "veach-bidir"),
                    Scene(os.path.join(scene_path, "veach-bidir"), "mts1_gpt.xml", "veach-bidir"),

                    Scene(os.path.join(scene_path, "veach-door"), "mts1_path.xml", "veach-door"),
                    Scene(os.path.join(scene_path, "veach-door"), "mts1_gpt.xml", "veach-door"),

                    ]


    mitsuba_path = os.path.abspath("path/to/executable")




    for s in scene_list:

        executable = os.path.join(mitsuba_path, "mitsuba")

        scene = os.path.join(s.path, s.xml)

        output_name = s.scene_name+"_"+s.xml.split(".")[0]
        output = "-o "+output_name


        command = executable + " " + scene + " "  + " " + output


        os.system(command)
        print()
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("===========================================================")
        print()
