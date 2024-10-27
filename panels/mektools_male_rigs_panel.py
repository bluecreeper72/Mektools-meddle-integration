import bpy
from bpy.types import Panel

class MEKTOOLS_PT_MaleRigs(Panel):
    bl_label = "Male Rigs"
    bl_idname = "MEKTOOLS_PT_MaleRigs"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_options = {'HIDE_HEADER'}

    def draw(self, context):
        layout = self.layout
        layout.operator("mektools.import_mekrig_midlander_male", text="Midlander Male")
        layout.operator("mektools.import_mekrig_highlander_male", text="Highlander Male")
        layout.operator("mektools.import_mekrig_elezen_male", text="Elezen Male")
        layout.operator("mektools.import_mekrig_miqote_male", text="Miqote Male")
        layout.operator("mektools.import_mekrig_roegadyn_male", text="Roegadyn Male")
        layout.operator("mektools.import_mekrig_aura_male", text="Aura Male")
        layout.operator("mektools.import_mekrig_hrothgar_male", text="Hrothgar Male")
        layout.operator("mektools.import_mekrig_viera_male", text="Viera Male")
        layout.operator("mektools.import_mekrig_lalafell_male", text="Lalafell Male")  # Lalafell Male button

def register():
    bpy.utils.register_class(MEKTOOLS_PT_MaleRigs)

def unregister():
    bpy.utils.unregister_class(MEKTOOLS_PT_MaleRigs)
