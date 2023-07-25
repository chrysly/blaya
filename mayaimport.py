import maya.cmds as cmds
import sys

mainPath = os.path.join(cmds.workspace(q=True, rd=True), 'scripts/Blaya')
print(mainPath)
sys.path.append(mainPath)

import pathwriter as writer

shelf_name = 'Custom'
if not cmds.shelfLayout(shelf_name, q = True, exists = True):
    raise RuntimeError("Shelf '{}' not found".format(shelf_name))
   
new_shelf_button = cmds.shelfButton(i = 'fileOpen.png', label = "Blaya", parent = shelf_name, noDefaultPopup = True)
popup_menu = cmds.popupMenu(parent = new_shelf_button, button = 3)

def import_fbx(self):
    file_path = writer.readDirectory(mainPath)
    new_nodes = cmds.file(file_path, i = True, rnn = True)
    if not new_nodes:
        cmds.file(file_path, mnc = False, reference = True)
        cmds.file(file_path, importReference = True)

menu_command_1 = cmds.menuItem(label="Import From Blender", sourceType="python", parent=popup_menu, command=import_fbx)