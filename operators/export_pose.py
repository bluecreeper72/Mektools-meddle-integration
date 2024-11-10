import bpy
import json
import os
from bpy.types import Operator
from bpy.props import StringProperty
from bpy_extras.io_utils import ExportHelper

class EXPORT_OT_ExportPose(Operator, ExportHelper):
    bl_idname = "export_skeleton.pose"
    bl_label = "Export Skeleton Pose to POSE"

    filename_ext = '.pose'
    filter_glob: StringProperty(default='*.pose', options={'HIDDEN'})

    def execute(self, context):
        # Load bone groups from JSON
        json_path = os.path.join(os.path.dirname(__file__), "..\data", "bone_groups.json")
        with open(json_path) as f:
            bone_groups = json.load(f)
        
        # Get selected groups from the panel
        props = context.scene.bone_group_props
        selected_groups = {group for group in bone_groups if getattr(props, group, False)}
        
        # Prepare data for export
        armature = context.object
        if not armature or armature.type != 'ARMATURE':
            self.report({'ERROR'}, "No armature selected")
            return {'CANCELLED'}
        
        # Root bone assumed as "root"
        root_bone = armature.pose.bones.get("root")
        if not root_bone:
            self.report({'ERROR'}, "Root bone 'root' not found")
            return {'CANCELLED'}
        
        root_matrix_world = armature.matrix_world @ root_bone.matrix
        skeleton_data = {
            "FileExtension": ".pose",
            "TypeName": "Ktisis Pose",
            "FileVersion": 2,
            "Position": f"{root_matrix_world.translation.x:.6f}, {root_matrix_world.translation.y:.6f}, {root_matrix_world.translation.z:.6f}",
            "Rotation": f"{root_matrix_world.to_quaternion().x:.6f}, {root_matrix_world.to_quaternion().y:.6f}, {root_matrix_world.to_quaternion().z:.6f}, {root_matrix_world.to_quaternion().w:.6f}",
            "Scale": f"{root_matrix_world.to_scale().x:.6f}, {root_matrix_world.to_scale().y:.6f}, {root_matrix_world.to_scale().z:.6f}",
            "Bones": {}
        }

        # Collect data for selected groups
        for group in selected_groups:
            for bone_name in bone_groups[group]:
                bone = armature.pose.bones.get(bone_name)
                if bone:
                    bone_matrix_world = armature.matrix_world @ bone.matrix
                    relative_matrix = root_matrix_world.inverted() @ bone_matrix_world

                    bone_data = {
                        "Position": f"{relative_matrix.translation.x:.6f}, {relative_matrix.translation.y:.6f}, {relative_matrix.translation.z:.6f}",
                        "Rotation": f"{relative_matrix.to_quaternion().x:.6f}, {relative_matrix.to_quaternion().y:.6f}, {relative_matrix.to_quaternion().z:.6f}, {relative_matrix.to_quaternion().w:.6f}",
                        "Scale": f"{relative_matrix.to_scale().x:.8f}, {relative_matrix.to_scale().y:.8f}, {relative_matrix.to_scale().z:.8f}"
                    }
                    skeleton_data["Bones"][bone_name] = bone_data
        
        # Write to the file
        with open(self.filepath, 'w') as f:
            json.dump(skeleton_data, f, indent=4)
        
        self.report({'INFO'}, "Pose exported successfully!")
        return {'FINISHED'}

def register():
    bpy.utils.register_class(EXPORT_OT_ExportPose)

def unregister():
    bpy.utils.unregister_class(EXPORT_OT_ExportPose)