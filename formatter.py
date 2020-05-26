import os

for i in os.listdir('ApplyingToCollege'):
    path = "ApplyingToCollege/" + i
    if ".png" not in (str(open(path))) and "jpg" not in (str(open(path))):
        os.rename(path, path.replace(".md", ".txt"))