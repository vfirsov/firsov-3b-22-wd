import os

directory = "my_folder"

path = os.path.join('./', directory)

os.mkdir(path)

print("Directory '% s' created" % directory)
