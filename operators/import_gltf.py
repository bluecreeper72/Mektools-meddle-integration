# type: ignore
import bpy
from bpy.types import Operator  # type: ignore
from bpy.props import StringProperty  # type: ignore




class IMPORT_OT_CustomGLTFImport(Operator):
    """Custom GLTF Import Operator"""
    bl_idname = "import_scene.custom_gltf"
    bl_label = "Import GLTF/GLB and Process"
    bl_options = {'REGISTER', 'UNDO'}

    filepath: StringProperty(subtype="FILE_PATH")

    def execute(self, context):
        bpy.ops.import_scene.gltf(filepath=self.filepath)

        for obj in bpy.data.objects:
            if obj.name == "Icosphere":
                bpy.data.objects.remove(obj, do_unlink=True)

        if "glTF_not_exported" in bpy.data.collections:
            bpy.data.collections.remove(bpy.data.collections["glTF_not_exported"])

        armature_obj = next((obj for obj in bpy.context.scene.objects if obj.type == 'ARMATURE'), None)
        if armature_obj:
            bpy.context.view_layer.objects.active = armature_obj
            bpy.ops.object.mode_set(mode='POSE')
            bpy.ops.pose.select_all(action='SELECT')
            bpy.ops.pose.transforms_clear()

            if armature_obj.animation_data and armature_obj.animation_data.action:
                action = armature_obj.animation_data.action
                for fcurve in action.fcurves:
                    action.fcurves.remove(fcurve)

            bpy.ops.object.mode_set(mode='OBJECT')
        
        return {'FINISHED'}

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

def register():
    bpy.utils.register_class(IMPORT_OT_CustomGLTFImport)

def unregister():
    bpy.utils.unregister_class(IMPORT_OT_CustomGLTFImport)
