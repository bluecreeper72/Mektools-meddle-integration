import bpy
from bpy.types import Panel, Operator
    
class VIEW3D_PT_ExportPose(Panel):
    bl_idname = "VIEW3D_PT_ExportPose"
    bl_label = "Pose Export"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Mektools"
    bl_description = "Exports current pose to a .pose file"

    def draw(self, context):
        layout = self.layout

        # Export current selected Armature as .pose file
        layout.operator("export_skeleton.pose", text="Export as Gpose")
        
def register():
    bpy.utils.register_class(VIEW3D_PT_ExportPose)

def unregister():
    bpy.utils.unregister_class(VIEW3D_PT_ExportPose)