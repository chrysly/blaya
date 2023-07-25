import maya.cmds as cmds
import sys
import os

path = os.path.expanduser('~\Documents')
directory = 'Blaya Source\_path.txt'
path = os.path.join(path, directory)

shelf_name = 'Custom'
if not cmds.shelfLayout(shelf_name, q = True, exists = True):
    raise RuntimeError("Shelf '{}' not found".format(shelf_name))
   
new_shelf_button = cmds.shelfButton(i = 'fileOpen.png', label = "Blaya", parent = shelf_name, noDefaultPopup = True)
popup_menu = cmds.popupMenu(parent = new_shelf_button, button = 3)

def import_fbx(self):
    file_path = readDirectory()
    new_nodes = cmds.file(file_path, i = True, rnn = True)
    if not new_nodes:
        cmds.file(file_path, mnc = False, reference = True)
        cmds.file(file_path, importReference = True)

menu_command_1 = cmds.menuItem(label="Import From Blender", sourceType="python", parent=popup_menu, command=import_fbx)

def readDirectory():
    with open(path, 'r') as file:
        return file.readline()