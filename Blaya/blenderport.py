bl_info = {
    "name" : "Maya Bridge (Blender Port)",
    "author" : "chrysly",
    "version" : (1, 0),
    "blender" : (3, 6, 1),
    "location" : "View3d > Tool",
    "warning" : "",
    "wiki_url" : "",
    "category" : "3D View",
}

import bpy
import os
import subprocess
import sys

#scriptFile = os.path.dirname(os.path.abspath(__file__))
#mainPath = scriptFile
#mainPath = os.path.dirname(bpy.context.space_data.text.filepath)
#sys.path.append(mainPath)

#import pathwriter as writer

class MayaPanel(bpy.types.Panel):
    bl_label = "Maya Bridge"
    bl_idname = "PT_Maya"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Maya'
    
    def draw(self, context):
        layout = self.layout
    
        row = layout.row()
        row.operator("object.select_mesh", icon = 'RESTRICT_SELECT_OFF')
        row = layout.row()
        row.operator("ops.export_selected_maya", icon = 'EXPORT', text = "Selected To Queue")

class SelectAllMesh(bpy.types.Operator):
    """Selects all mesh objects in scene"""
    bl_idname = "object.select_mesh"
    bl_label = "Select All Meshes"
    
    def execute(self, context):
        objects = bpy.context.scene.objects
        for obj in objects:
            obj.select_set(obj.type == "MESH")
        return {'FINISHED'}

class ExportSelectedToMaya(bpy.types.Operator):
    """Exports all selected meshes, and sends to Maya.
       *Does not automatically save the scene"""
    bl_idname = "ops.export_selected_maya"
    bl_label = "Export To Maya"
    
    def execute(self, context):
        export_selected()
        return {'FINISHED'}
        
def export_selected():
    path, ext = os.path.splitext(bpy.data.filepath)
    path += '.fbx'
    #writer.writeDirectory(path, mainPath)
    writeSourceDirectory(path)
    bpy.ops.export_scene.fbx(filepath = path, use_selection=True)

def writeSourceDirectory(path):
    srcPath = os.path.expanduser('~\Documents')
    directory = 'Blaya Source'

    if not os.path.exists(os.path.join(srcPath, directory)):
        os.makedirs(os.path.join(srcPath, directory))
        
    txtDirectory = '_path.txt'
    folder = os.path.join(srcPath, directory)
    txtDirectory = os.path.join(folder, txtDirectory)
    
    with open(txtDirectory, 'w+') as file:
        file.write(path)

def register():
    bpy.utils.register_class(MayaPanel)
    bpy.utils.register_class(SelectAllMesh)
    bpy.utils.register_class(ExportSelectedToMaya)
def unregister():
    bpy.utils.unregister_class(MayaPanel)
    bpy.utils.unregister_class(SelectAllMesh)
    bpy.utils.unregister_class(ExportSelectedToMaya)

if __name__ == "__main__":
    register()