import os
import markdown
from bs4 import UnicodeDammit
files = []

z = 1

for i in os.listdir('ApplyingToCollege'):
    path = "ApplyingToCollege/" + i
    if ".png" not in (str(open(path))) and "jpg" not in (str(open(path))):

        try:
            print(open(path).read())
        except UnicodeDecodeError:
            print(path + " error number " + str(z) + " has occurred ")
            z += 1
