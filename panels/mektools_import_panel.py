import bpy
from bpy.types import Panel

class VIEW3D_PT_ImportPanel(Panel):
    bl_label = "Import"
    bl_idname = "VIEW3D_PT_import_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'NOR'

    def draw(self, context):
        layout = self.layout

        # Import Options
        row = layout.row(align=True)
        row.operator("mektools.import_meddle_gltf", text="GLTF from Meddle")
        row.operator("mektools.import_textools_fbx", text="FBX from TexTools")

        # Shader Append Button
        layout.operator("mektools.append_shaders", text="Append Shaders", icon="SHADING_TEXTURE")

        # Rigs Label and Popovers for Male and Female Rigs
        layout.separator()
        layout.label(text="Rigs")
        split = layout.split(factor=0.5, align=True)
        split.popover("MEKTOOLS_PT_MaleRigs", text="Male", icon_value=0)
        split.popover("MEKTOOLS_PT_FemaleRigs", text="Female", icon_value=0)

def register():
    bpy.utils.register_class(VIEW3D_PT_ImportPanel)

def unregister():
    bpy.utils.unregister_class(VIEW3D_PT_ImportPanel)
