# type: ignore
import bpy
import os
from bpy.types import Operator
from ..data.racial_codes import racial_code_mapping

class IMPORT_OT_AppendCollection(Operator):
    """Append the appropriate collection based on the character's racial code"""
    bl_idname = "import_scene.append_collection"
    bl_label = "Append Collection by Racial Code"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # Locate the 'iri' object in the scene
        iri_object = next((obj for obj in bpy.data.objects if "iri" in obj.name), None)
        
        if not iri_object:
            self.report({'WARNING'}, "No 'iri' object found in the scene.")
            return {'CANCELLED'}

        # Extract the racial code from the 'iri' object's name
        iri_name = iri_object.name
        racial_code = iri_name[iri_name.find("c"):iri_name.find("c")+5]  # Extracts something like 'c0801'

        # Map racial code to descriptive race name from racial_code_mapping
        race_name = racial_code_mapping.get(racial_code)
        
        if not race_name:
            self.report({'WARNING'}, f"No matching racial code for {racial_code}")
            return {'CANCELLED'}
        
        # Construct the .blend file path using the descriptive name
        blend_file_name = f"{race_name}.blend"
        addon_path = os.path.dirname(os.path.abspath(__file__))
        assets_path = os.path.join(addon_path, "..", "assets", blend_file_name)
        
        if not os.path.exists(assets_path):
            self.report({'WARNING'}, f"No .blend file found for {blend_file_name}")
            return {'CANCELLED'}

        collection_name = race_name

        # Link the collection from the blend file
        with bpy.data.libraries.load(assets_path, link=False) as (data_from, data_to):
            if collection_name in data_from.collections:
                data_to.collections.append(collection_name)
            else:
                self.report({'WARNING'}, f"Collection '{collection_name}' not found in {blend_file_name}")
                return {'CANCELLED'}

        # Add the appended collection to the scene
        appended_collection = bpy.data.collections.get(collection_name)
        if appended_collection:
            context.scene.collection.children.link(appended_collection)
            self.report({'INFO'}, f"Appended '{collection_name}' from {blend_file_name}")
        else:
            self.report({'WARNING'}, f"Failed to append collection '{collection_name}'")

        return {'FINISHED'}

def register():
    bpy.utils.register_class(IMPORT_OT_AppendCollection)

def unregister():
    bpy.utils.unregister_class(IMPORT_OT_AppendCollection)
