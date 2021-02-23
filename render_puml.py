import os
from subprocess import call
import shutil

for file in os.listdir('src'):
    if file.endswith('.puml'):
        call(["java", "-jar", "plantuml.jar", "src/" + file])
        fname = ''.join(file.split('.')[:-1]) + ".png"
        shutil.move("src/" + fname, "img/" + fname)

