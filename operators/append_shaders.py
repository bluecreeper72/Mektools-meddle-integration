# type: ignore
import bpy
import os
from bpy.types import Operator

class IMPORT_OT_AppendShaders(Operator):
    """Append all shaders from shaders.blend if they do not already exist"""
    bl_idname = "import_scene.append_shaders"
    bl_label = "Append Shaders"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # Path to the shaders.blend file
        addon_path = os.path.dirname(os.path.abspath(__file__))
        shaders_path = os.path.join(addon_path, "..", "assets", "shaders.blend")

        if not os.path.exists(shaders_path):
            self.report({'WARNING'}, "shaders.blend file not found in assets folder.")
            return {'CANCELLED'}

        # Load and append materials
        with bpy.data.libraries.load(shaders_path, link=False) as (data_from, data_to):
            # Find materials that don't exist yet in the current scene
            materials_to_append = [mat for mat in data_from.materials if mat not in bpy.data.materials]
            data_to.materials = materials_to_append

        # Report success
        if materials_to_append:
            self.report({'INFO'}, f"Appended {len(materials_to_append)} new materials from shaders.blend.")
        else:
            self.report({'INFO'}, "All materials from shaders.blend already exist in the scene.")

        return {'FINISHED'}

def register():
    bpy.utils.register_class(IMPORT_OT_AppendShaders)

def unregister():
    bpy.utils.unregister_class(IMPORT_OT_AppendShaders)
