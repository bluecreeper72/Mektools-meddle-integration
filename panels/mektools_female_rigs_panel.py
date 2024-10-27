import bpy
from bpy.types import Panel

class MEKTOOLS_PT_FemaleRigs(Panel):
    bl_label = "Female Rigs"
    bl_idname = "MEKTOOLS_PT_FemaleRigs"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_options = {'HIDE_HEADER'}

    def draw(self, context):
        layout = self.layout
        layout.operator("mektools.import_mekrig_midlander_female", text="Midlander Female")
        layout.operator("mektools.import_mekrig_highlander_female", text="Highlander Female")
        layout.operator("mektools.import_mekrig_elezen_female", text="Elezen Female")
        layout.operator("mektools.import_mekrig_miqote_female", text="Miqote Female")
        layout.operator("mektools.import_mekrig_roegadyn_female", text="Roegadyn Female")
        layout.operator("mektools.import_mekrig_aura_female", text="Aura Female")
        layout.operator("mektools.import_mekrig_viera_female", text="Viera Female")
        layout.operator("mektools.import_mekrig_lalafell_female", text="Lalafell Female")  # Lalafell Female button

def register():
    bpy.utils.register_class(MEKTOOLS_PT_FemaleRigs)

def unregister():
    bpy.utils.unregister_class(MEKTOOLS_PT_FemaleRigs)
