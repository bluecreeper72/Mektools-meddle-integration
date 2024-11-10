import bpy
from bpy.types import Panel, PropertyGroup
from bpy.props import BoolProperty

class BoneGroupProperties(PropertyGroup):
    HandsLeft: BoolProperty(name="HandsLeft", default=False)
    HandsRight: BoolProperty(name="HandsRight", default=False)

class VIEW3D_PT_ExportPose(Panel):
    bl_idname = "VIEW3D_PT_ExportPose"
    bl_label = "Pose Export"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Mektools"

    def draw(self, context):
        layout = self.layout
        props = context.scene.bone_group_props
        
        # Checkboxes for each group
        layout.prop(props, "HandsLeft", text="Hands Left")
        layout.prop(props, "HandsRight", text="Hands Right")
        layout.prop(props, "Face", text="Face")
        layout.prop(props, "Hair", text="Hair")
        layout.prop(props, "Tail", text="Tail")
        layout.prop(props, "Body", text="Body")
        
        # Export button
        layout.operator("export_skeleton.pose", text="Export Selected Groups")

def register():
    bpy.utils.register_class(BoneGroupProperties)
    bpy.types.Scene.bone_group_props = bpy.props.PointerProperty(type=BoneGroupProperties)
    bpy.utils.register_class(VIEW3D_PT_ExportPose)

def unregister():
    bpy.utils.unregister_class(VIEW3D_PT_ExportPose)
    bpy.utils.unregister_class(BoneGroupProperties)
    del bpy.types.Scene.bone_group_props