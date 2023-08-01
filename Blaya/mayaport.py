import maya.cmds as cmds
import sys
import os

path = os.path.expanduser('~\Documents')
directory = 'Blaya Source\_path.txt'
path = os.path.join(path, directory)

def readDirectory():
    with open(path, 'r') as file:
        return file.readline()

def refExists():
    for ref in cmds.ls(type = 'reference'):
        refName = cmds.referenceQuery(ref, filename = True)
        if os.path.samefile(str(refName), str(readDirectory())):
            return True
    return False

try:
    file_path = readDirectory()
    if (file_path != ""):
        if (refExists() == True):
            for ref in cmds.ls(type = 'reference'):
                i += 1 
                cmds.file(loadReference = ref)
        else:
            new_nodes = cmds.file(file_path, reference = True)
except:
    print("Empty reference")

with open(path, 'w+') as file:
        file.write("")