import os
from subprocess import call
import shutil

for file in os.listdir('src'):
    if file.endswith('.puml') and not 'theme' in file:
        call(["java", "-jar", "plantuml.jar", "-config", "src/ferrytix_theme.puml", "src/" + file])
        fname = ''.join(file.split('.')[:-1]) + ".png"
        shutil.move("src/" + fname, "img/" + fname)

