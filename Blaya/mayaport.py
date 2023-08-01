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

file_path = readDirectory()
if (True):
    if (refExists() == True):
        for ref in cmds.ls(type = 'reference'):
            try:
                cmds.file(loadReference = ref)
            except:
                print("Empty reference")
    else:
        new_nodes = cmds.file(file_path, reference = True)