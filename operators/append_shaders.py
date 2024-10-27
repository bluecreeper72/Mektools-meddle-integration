import bpy
from bpy.types import Operator

class MEKTOOLS_OT_AppendShaders(Operator):
    bl_idname = "mektools.append_shaders"
    bl_label = "Append Shaders"
    bl_description = "Append Shaders from WOL Shaders by Skulblaka"  # Tooltip text

    def execute(self, context):
        self.report({'INFO'}, "Placeholder for Append Shaders")
        return {'FINISHED'}

def register():
    bpy.utils.register_class(MEKTOOLS_OT_AppendShaders)

def unregister():
    bpy.utils.unregister_class(MEKTOOLS_OT_AppendShaders)
