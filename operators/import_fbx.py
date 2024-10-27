# type: ignore
import bpy
from bpy.types import Operator
from bpy.props import StringProperty

class IMPORT_OT_TexToolsFBX(Operator):
    """Import FBX from TexTools"""
    bl_idname = "import_scene.textools_fbx"
    bl_label = "Import TexTools FBX"
    bl_options = {'REGISTER', 'UNDO'}

    filepath: StringProperty(subtype="FILE_PATH")

    def execute(self, context):
        bpy.ops.import_scene.fbx(filepath=self.filepath)
        
        # Custom setup specific to TexTools FBX files
        # Insert shader and transform setup code here

        return {'FINISHED'}

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

def register():
    bpy.utils.register_class(IMPORT_OT_TexToolsFBX)

def unregister():
    bpy.utils.unregister_class(IMPORT_OT_TexToolsFBX)
