import bpy
from bpy.types import Operator
import os

# Define the path to the assets folder relative to this file
ASSETS_PATH = os.path.join(os.path.dirname(__file__), "../assets")

class MEKTOOLS_OT_ImportMekrigBase(Operator):
    """Base class for importing Mekrig collections"""

    collection_name: str
    file_name: str

    def execute(self, context):
        # Construct the file path
        file_path = os.path.join(ASSETS_PATH, self.file_name)

        # Check if the .blend file exists
        if not os.path.exists(file_path):
            self.report({'ERROR'}, f"File not found: {file_path}")
            return {'CANCELLED'}

        # Load and append the specified collection from the .blend file
        with bpy.data.libraries.load(file_path, link=False) as (data_from, data_to):
            if self.collection_name in data_from.collections:
                data_to.collections = [self.collection_name]
            else:
                self.report({'WARNING'}, f"Collection '{self.collection_name}' not found in {file_path}")
                return {'CANCELLED'}

        # Link the collection to the current scene
        for collection in data_to.collections:
            bpy.context.scene.collection.children.link(collection)

        return {'FINISHED'}

# Example Operator for Midlander Male
class MEKTOOLS_OT_ImportMekrigMidlanderMale(MEKTOOLS_OT_ImportMekrigBase):
    bl_idname = "mektools.import_mekrig_midlander_male"
    bl_label = "Import Midlander Male Rig"
    collection_name = "Midlander Male"
    file_name = "Midlander Male.blend"

# Additional operators follow the same format...
class MEKTOOLS_OT_ImportMekrigHighlanderMale(MEKTOOLS_OT_ImportMekrigBase):
    bl_idname = "mektools.import_mekrig_highlander_male"
    bl_label = "Import Highlander Male Rig"
    collection_name = "Highlander Male"
    file_name = "Highlander Male.blend"

class MEKTOOLS_OT_ImportMekrigElezenMale(MEKTOOLS_OT_ImportMekrigBase):
    bl_idname = "mektools.import_mekrig_elezen_male"
    bl_label = "Import Elezen Male Rig"
    collection_name = "Elezen Male"
    file_name = "Elezen Male.blend"

# Continue this pattern for each race and gender...

def register():
    bpy.utils.register_class(MEKTOOLS_OT_ImportMekrigMidlanderMale)
    bpy.utils.register_class(MEKTOOLS_OT_ImportMekrigHighlanderMale)
    bpy.utils.register_class(MEKTOOLS_OT_ImportMekrigElezenMale)
    # Register other operators similarly...

def unregister():
    bpy.utils.unregister_class(MEKTOOLS_OT_ImportMekrigMidlanderMale)
    bpy.utils.unregister_class(MEKTOOLS_OT_ImportMekrigHighlanderMale)
    bpy.utils.unregister_class(MEKTOOLS_OT_ImportMekrigElezenMale)
    # Unregister other operators similarly...
