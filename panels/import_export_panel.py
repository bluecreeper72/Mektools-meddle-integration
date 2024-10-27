# type: ignore
import bpy
from bpy.types import Panel
from ..operators.import_mekrig import VIEW3D_OT_ToggleGender, IMPORT_OT_AppendMekrig

class VIEW3D_PT_ImportMekrigPanel(Panel):
    """Panel for Importing Mekrigs based on Gender and Race"""
    bl_label = "Import Mekrig"
    bl_idname = "VIEW3D_PT_import_mekrig_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'NOR'

    def draw(self, context):
        layout = self.layout

        # Header for Import Mekrig
        layout.label(text="Import Mekrig")

        # Gender selection buttons
        row = layout.row(align=True)
        row.operator("view3d.toggle_gender", text="Male").gender = "MALE"
        row.operator("view3d.toggle_gender", text="Female").gender = "FEMALE"

        # Display race options based on selected gender
        gender = context.scene.get("mekrig_gender")
        if gender:
            layout.label(text=f"{gender.title()} Mekrigs")

            # Add buttons for each race specific to the selected gender
            for code, name in racial_code_mapping.items():
                if gender.lower() in name.lower():  # Show only Male or Female races
                    layout.operator("import_scene.append_mekrig", text=name).race = code

def register():
    bpy.utils.register_class(VIEW3D_PT_ImportMekrigPanel)

def unregister():
    bpy.utils.unregister_class(VIEW3D_PT_ImportMekrigPanel)
