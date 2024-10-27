# type: ignore
import bpy
import os
from bpy.types import Operator, Panel
from bpy.props import EnumProperty
from ..data.racial_codes import racial_code_mapping

class VIEW3D_OT_ToggleGender(Operator):
    """Toggle between Male and Female Mekrig import options"""
    bl_idname = "view3d.toggle_gender"
    bl_label = "Toggle Gender"

    gender: EnumProperty(items=[("MALE", "Male", ""), ("FEMALE", "Female", "")])

    def execute(self, context):
        context.scene.mekrig_gender = self.gender  # Store the selected gender in the scene property
        return {'FINISHED'}

class IMPORT_OT_AppendMekrig(Operator):
    """Append the specified Mekrig collection"""
    bl_idname = "import_scene.append_mekrig"
    bl_label = "Append Mekrig"

    race: EnumProperty(items=[(code, name, "") for code, name in racial_code_mapping.items()])

    def execute(self, context):
        gender = context.scene.mekrig_gender.lower()  # Get selected gender (male or female)
        race_name = racial_code_mapping[self.race]

        # Construct the file path and collection name based on gender and race
        blend_file_name = f"{race_name}.blend"
        addon_path = os.path.dirname(os.path.abspath(__file__))
        assets_path = os.path.join(addon_path, "..", "assets", blend_file_name)
        
        if not os.path.exists(assets_path):
            self.report({'WARNING'}, f"{blend_file_name} not found in assets.")
            return {'CANCELLED'}

        collection_name = race_name  # Assuming each collection in the file matches the race name

        # Load and append collection from the blend file
        with bpy.data.libraries.load(assets_path, link=False) as (data_from, data_to):
            if collection_name in data_from.collections:
                data_to.collections.append(collection_name)
            else:
                self.report({'WARNING'}, f"Collection '{collection_name}' not found in {blend_file_name}")
                return {'CANCELLED'}

        # Link the appended collection to the scene
        appended_collection = bpy.data.collections.get(collection_name)
        if appended_collection:
            context.scene.collection.children.link(appended_collection)
            self.report({'INFO'}, f"Appended '{collection_name}' from {blend_file_name}")
        else:
            self.report({'WARNING'}, f"Failed to append collection '{collection_name}'")

        return {'FINISHED'}

def register():
    bpy.utils.register_class(VIEW3D_OT_ToggleGender)
    bpy.utils.register_class(IMPORT_OT_AppendMekrig)

def unregister():
    bpy.utils.unregister_class(VIEW3D_OT_ToggleGender)
    bpy.utils.unregister_class(IMPORT_OT_AppendMekrig)
