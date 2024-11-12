import bpy
from bpy.types import Operator
from bpy.props import StringProperty, EnumProperty
from bpy_extras.io_utils import ExportHelper

class EXPORT_ACTION_OT_gltf(Operator, ExportHelper):
    bl_idname = "export_action.gltf"
    bl_label = "Export GLTF with custom settings for FFXIV Animations"

    # Define file path property to allow users to select a path
    filename_ext = ".gltf"
    filter_glob: StringProperty(default="*.gltf", options={'HIDDEN'})

    # Property to select an action
    action_name: EnumProperty(
        name="Action",
        description="Select an action to export",
        items=lambda self, context: [(action.name, action.name, "") for action in bpy.data.actions]
    )

    def invoke(self, context, event):
        # Set the default file name to the selected action's name
        self.filepath = bpy.path.abspath(f"//{self.action_name}.gltf")
        return super().invoke(context, event)

    def execute(self, context):
        # Use the selected action as the default placeholder file name
        filepath = self.filepath if self.filepath else bpy.path.abspath(f"//{self.action_name}.gltf")

        # Set the active action in the context before exporting
        context.object.animation_data.action = bpy.data.actions.get(self.action_name)

        # Custom export settings
        bpy.ops.export_scene.gltf(
            filepath=filepath,
            export_format='GLTF_SEPARATE',
            export_apply=True,
            export_yup=True,
            export_animation=True,
            export_selected=True,
            use_selection=True,
            export_materials='EXPORT',
            export_frame_range=True, # Limit playback range
            export_force_sampling=True, # Keep all channels for bones/objects
            export_keep_anim_armature=True, # Only export active action for animation
            export_keep_anim_object=True
        )

        self.report({'INFO'}, f"GLTF exported to {filepath}")
        return {'FINISHED'}
    
class EXPORT_VFXOBJ_OT_gltf(Operator):
    bl_idname = "export_vfxobj.gltf"
    bl_label = "Export GLTF with custom settings for FFXIV VFX Models"

    def execute(self, context):
        filepath = bpy.path.abspath("//vfxobj.gltf")

        # Custom export settings
        bpy.ops.export_scene.gltf(
            filepath=filepath,
            export_format='GLTF_SEPARATE',
            export_apply=True,
            export_yup=True,
            export_animation=True,
            export_selected=True,
            use_selection=True,
            export_materials='EXPORT'
        )

        self.report({'INFO'}, f"GLTF exported to {filepath}")
        return {'FINISHED'}

# Register and unregister the operator
def register():
    bpy.utils.register_class(EXPORT_ACTION_OT_gltf)
    bpy.utils.register_class(EXPORT_VFXOBJ_OT_gltf)

def unregister():
    bpy.utils.unregister_class(EXPORT_ACTION_OT_gltf)
    bpy.utils.unregister_class(EXPORT_VFXOBJ_OT_gltf)