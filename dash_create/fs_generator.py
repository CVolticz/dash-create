#!/usr/bin/env python
# class use to generate full filestructure
import os
import shutil


class FSGenerator():
    # Constructor
    def __init__(self, cwd):
        # intial objects to be generate
        self.__cwd = cwd.replace("\\","/")
        self.__bin = (os.path.dirname(__file__)+"/bin/_fs").replace("\\","/")

    # clone existing fs and place if to 
    def generate_file_structure(self):
        shutil.copytree(self.__bin, self.__cwd)



if __name__=="__main__":
    """ Testing Purposes
    """
    obj = FSGenerator("./template")
    obj.generate_file_structure()