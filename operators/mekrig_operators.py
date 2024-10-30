import bpy
from bpy.types import Operator
import os

# Define the path to the assets folder relative to this file
ASSETS_PATH = os.path.join(os.path.dirname(__file__), "../assets")

class MEKTOOLS_OT_ImportMekrigBase(Operator):
    """Base class for importing Mekrig collections"""
    bl_options = {'REGISTER', 'UNDO', 'INTERNAL'}  # Add 'INTERNAL' to hide from UI

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

        self.report({'INFO'}, f"Successfully imported {self.collection_name}")
        return {'FINISHED'}

# Male Rig Operators
class MEKTOOLS_OT_ImportMekrigMidlanderMale(MEKTOOLS_OT_ImportMekrigBase):
    bl_idname = "mektools.import_mekrig_midlander_male"
    # bl_label = "Import Midlander Male Rig"
    bl_options = {'INTERNAL'}
    collection_name = "Midlander Male"
    file_name = "Midlander Male.blend"

class MEKTOOLS_OT_ImportMekrigHighlanderMale(MEKTOOLS_OT_ImportMekrigBase):
    bl_idname = "mektools.import_mekrig_highlander_male"
    # bl_label = "Import Highlander Male Rig"
    bl_options = {'INTERNAL'}
    collection_name = "Highlander Male"
    file_name = "Highlander Male.blend"

class MEKTOOLS_OT_ImportMekrigElezenMale(MEKTOOLS_OT_ImportMekrigBase):
    bl_idname = "mektools.import_mekrig_elezen_male"
    # bl_label = "Import Elezen Male Rig"
    bl_options = {'INTERNAL'}
    collection_name = "Elezen Male"
    file_name = "Elezen Male.blend"

class MEKTOOLS_OT_ImportMekrigMiqoteMale(MEKTOOLS_OT_ImportMekrigBase):
    bl_idname = "mektools.import_mekrig_miqote_male"
    # bl_label = "Import Miqote Male Rig"
    bl_options = {'INTERNAL'}
    collection_name = "Miqote Male"
    file_name = "Miqote Male.blend"

class MEKTOOLS_OT_ImportMekrigRoegadynMale(MEKTOOLS_OT_ImportMekrigBase):
    bl_idname = "mektools.import_mekrig_roegadyn_male"
    # bl_label = "Import Roegadyn Male Rig"
    bl_options = {'INTERNAL'}
    collection_name = "Roegadyn Male"
    file_name = "Roegadyn Male.blend"

class MEKTOOLS_OT_ImportMekrigAuraMale(MEKTOOLS_OT_ImportMekrigBase):
    bl_idname = "mektools.import_mekrig_aura_male"
    # bl_label = "Import Aura Male Rig"
    bl_options = {'INTERNAL'}
    collection_name = "Aura Male"
    file_name = "Aura Male.blend"

class MEKTOOLS_OT_ImportMekrigHrothgarMale(MEKTOOLS_OT_ImportMekrigBase):
    bl_idname = "mektools.import_mekrig_hrothgar_male"
    # bl_label = "Import Hrothgar Male Rig"
    bl_options = {'INTERNAL'}
    collection_name = "Hrothgar Male"
    file_name = "Hrothgar Male.blend"

class MEKTOOLS_OT_ImportMekrigVieraMale(MEKTOOLS_OT_ImportMekrigBase):
    bl_idname = "mektools.import_mekrig_viera_male"
    # bl_label = "Import Viera Male Rig"
    bl_options = {'INTERNAL'}
    collection_name = "Viera Male"
    file_name = "Viera Male.blend"

# Lalafell Rig Operators (both male and female point to the same file and collection)
class MEKTOOLS_OT_ImportMekrigLalafellMale(MEKTOOLS_OT_ImportMekrigBase):
    bl_idname = "mektools.import_mekrig_lalafell_male"
    # bl_label = "Import Lalafell Male Rig"
    bl_options = {'INTERNAL'}
    collection_name = "Lalafell"
    file_name = "Lalafell.blend"

class MEKTOOLS_OT_ImportMekrigLalafellFemale(MEKTOOLS_OT_ImportMekrigBase):
    bl_idname = "mektools.import_mekrig_lalafell_female"
    # bl_label = "Import Lalafell Female Rig"
    bl_options = {'INTERNAL'}
    collection_name = "Lalafell"
    file_name = "Lalafell.blend"

# Female Rig Operators
class MEKTOOLS_OT_ImportMekrigMidlanderFemale(MEKTOOLS_OT_ImportMekrigBase):
    bl_idname = "mektools.import_mekrig_midlander_female"
    # bl_label = "Import Midlander Female Rig"
    bl_options = {'INTERNAL'}
    collection_name = "Midlander Female"
    file_name = "Midlander Female.blend"

class MEKTOOLS_OT_ImportMekrigHighlanderFemale(MEKTOOLS_OT_ImportMekrigBase):
    bl_idname = "mektools.import_mekrig_highlander_female"
    # bl_label = "Import Highlander Female Rig"
    bl_options = {'INTERNAL'}
    collection_name = "Highlander Female"
    file_name = "Highlander Female.blend"

class MEKTOOLS_OT_ImportMekrigElezenFemale(MEKTOOLS_OT_ImportMekrigBase):
    bl_idname = "mektools.import_mekrig_elezen_female"
    # bl_label = "Import Elezen Female Rig"
    bl_options = {'INTERNAL'}
    collection_name = "Elezen Female"
    file_name = "Elezen Female.blend"

class MEKTOOLS_OT_ImportMekrigMiqoteFemale(MEKTOOLS_OT_ImportMekrigBase):
    bl_idname = "mektools.import_mekrig_miqote_female"
    # bl_label = "Import Miqote Female Rig"
    bl_options = {'INTERNAL'}
    collection_name = "Miqote Female"
    file_name = "Miqote Female.blend"

class MEKTOOLS_OT_ImportMekrigRoegadynFemale(MEKTOOLS_OT_ImportMekrigBase):
    bl_idname = "mektools.import_mekrig_roegadyn_female"
    # bl_label = "Import Roegadyn Female Rig"
    bl_options = {'INTERNAL'}
    collection_name = "Roegadyn Female"
    file_name = "Roegadyn Female.blend"

class MEKTOOLS_OT_ImportMekrigAuraFemale(MEKTOOLS_OT_ImportMekrigBase):
    bl_idname = "mektools.import_mekrig_aura_female"
    # bl_label = "Import Aura Female Rig"
    bl_options = {'INTERNAL'}
    collection_name = "Aura Female"
    file_name = "Aura Female.blend"

class MEKTOOLS_OT_ImportMekrigHrothgarFemale(MEKTOOLS_OT_ImportMekrigBase):
    bl_idname = "mektools.import_mekrig_hrothgar_female"
    # bl_label = "Import Hrothgar Female Rig"
    bl_options = {'INTERNAL'}
    collection_name = "Hrothgar Female"
    file_name = "Hrothgar Female.blend"

class MEKTOOLS_OT_ImportMekrigVieraFemale(MEKTOOLS_OT_ImportMekrigBase):
    bl_idname = "mektools.import_mekrig_viera_female"
    # bl_label = "Import Viera Female Rig"
    bl_options = {'INTERNAL'}
    collection_name = "Viera Female"
    file_name = "Viera Female.blend"

# List of all classes to register and unregister
classes = [
    MEKTOOLS_OT_ImportMekrigMidlanderMale, MEKTOOLS_OT_ImportMekrigHighlanderMale, MEKTOOLS_OT_ImportMekrigElezenMale, MEKTOOLS_OT_ImportMekrigMiqoteMale, MEKTOOLS_OT_ImportMekrigRoegadynMale, MEKTOOLS_OT_ImportMekrigAuraMale, MEKTOOLS_OT_ImportMekrigHrothgarMale, MEKTOOLS_OT_ImportMekrigVieraMale, MEKTOOLS_OT_ImportMekrigLalafellMale, MEKTOOLS_OT_ImportMekrigLalafellFemale, MEKTOOLS_OT_ImportMekrigMidlanderFemale, MEKTOOLS_OT_ImportMekrigHighlanderFemale, MEKTOOLS_OT_ImportMekrigElezenFemale, MEKTOOLS_OT_ImportMekrigMiqoteFemale, MEKTOOLS_OT_ImportMekrigRoegadynFemale, MEKTOOLS_OT_ImportMekrigAuraFemale, MEKTOOLS_OT_ImportMekrigHrothgarFemale, MEKTOOLS_OT_ImportMekrigVieraFemale
]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
