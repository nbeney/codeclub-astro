import os
import sys


def path_for(filename):
    program_path = sys.argv[0]
    progam_dir = os.path.dirname(program_path)
    resource_path = os.path.join(progam_dir, "resources", filename)
    return resource_path


def find_images_in_dir(dir, extension=".png"):
    images = []
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        if os.path.isfile(path) and name.endswith(extension):
            images.append(path)
    return images
