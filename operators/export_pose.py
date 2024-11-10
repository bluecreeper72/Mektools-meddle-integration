import bpy
import json
import os
from os import path
from mathutils import *
from bpy_extras.io_utils import ExportHelper

def bone_filter(bone_name):
    #Returns True if the bone should be included in the export,
    #otherwise returns False.
    # Skip bones that start with "j_ex"
    #return not bone_name.startswith("j_ex")]
    return True

class EXPORT_OT_ExportPose(bpy.types.Operator, ExportHelper):
    bl_idname = "export_skeleton.pose"
    bl_label = "Export Skeleton Pose to POSE"
    
    filepath: bpy.props.StringProperty(subtype="FILE_PATH")
    filename_ext='.pose'
    filter_glob: bpy.props.StringProperty(
        default='*.pose',
        options={'HIDDEN'}
    )

    def execute(self, context):
        armature = bpy.context.object  # Ensure the active object is the armature
        if armature and armature.type == 'ARMATURE':
            origin_bone = armature.pose.bones.get("n_throw")  # Assuming "origin_root" is the relative ankor point

            if origin_bone:
                # Get the origin bone's transformation in world space
                origin_bone_matrix_world = armature.matrix_world @ origin_bone.matrix

                # Decompose origin bone matrix to position, rotation, and scale for top-level attributes
                origin_pos = origin_bone_matrix_world.to_translation()
                origin_rot = origin_bone_matrix_world.to_quaternion()
                origin_scale = origin_bone_matrix_world.to_scale()

                skeleton_data = {
                    "FileExtension": ".pose",
                    "TypeName": "Ktisis Pose",
                    "FileVersion": 2,
                    "Position": f"{origin_pos.x:.6f}, {origin_pos.y:.6f}, {origin_pos.z:.6f}",
                    "Rotation": f"{origin_rot.x:.6f}, {origin_rot.y:.6f}, {origin_rot.z:.6f}, {origin_rot.w:.6f}",
                    "Scale": f"{origin_scale.x:.6f}, {origin_scale.y:.6f}, {origin_scale.z:.6f}",
                    "Bones": {}
                }

                for bone in armature.pose.bones:
                    # Apply the bone filter
                    if not bone_filter(bone.name):
                        continue  # Skip bones that don't pass the filter
                    
                    # Get the bone's transformation in world space
                    bone_matrix_world = armature.matrix_world @ bone.matrix
                    
                    # Calculate the relative matrix to the origin bone
                    relative_matrix = origin_bone_matrix_world.inverted() @ bone_matrix_world

                    # Decompose the relative matrix to position, rotation, and scale
                    pos = relative_matrix.to_translation()
                    rot = relative_matrix.to_quaternion()
                    scale = relative_matrix.to_scale()

                    # Format transformations for JSON/POSE
                    bone_data = {
                        "Position": f"{pos.x:.6f}, {pos.y:.6f}, {pos.z:.6f}",
                        "Rotation": f"{rot.x:.6f}, {rot.y:.6f}, {rot.z:.6f}, {rot.w:.6f}",
                        "Scale": f"{scale.x:.8f}, {scale.y:.8f}, {scale.z:.8f}"  # Higher precision
                    }

                    # Add bone data to the skeleton
                    skeleton_data["Bones"][bone.name] = bone_data

            else:
                self.report({'ERROR'}, "origin bone 'n_throw' not found")
                return {'CANCELLED'}

        # Save to POSE
        with open(self.filepath, 'w') as f:
            json.dump(skeleton_data, f, indent=4)

        self.report({'INFO'}, "Pose exported successfully!")
        return {'FINISHED'}

# Register and unregister classes
def register():
    bpy.utils.register_class(EXPORT_OT_ExportPose)
    
def unregister():
    bpy.utils.unregister_class(EXPORT_OT_ExportPose)