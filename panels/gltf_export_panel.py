import bpy
from bpy.types import Panel, Operator

class VIEW3D_PT_GLTFExport(Panel):
    bl_idname = "VIEW3D_PT_GLTFExport"
    bl_label = "GLTF Export"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Mektools"
    bl_description = "Exports selected animation as glTF with custom settings"

    def draw(self, context):
        layout = self.layout
        layout.operator("export_action.gltf", text="Animation Export")
        layout.operator("export_vfxobj.gltf", text="VFX Model Export")



def register():
    bpy.utils.register_class(VIEW3D_PT_GLTFExport)

def unregister():
    bpy.utils.unregister_class(VIEW3D_PT_GLTFExport)
