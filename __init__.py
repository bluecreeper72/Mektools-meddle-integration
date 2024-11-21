import bpy
import json
import os

from .panels import (
    mektools_support_community_panel, 
    mektools_import_panel,
    pose_export_panel,
    glb_export_panel
)
from .operators import (
    import_meddle_gltf, 
    import_textools_fbx, 
    export_pose,       #.pose file export 
    export_glb,       # different gltf exports
    mekrig_operators,  # Consolidated operators for each Mekrig import
    append_shaders,
    lizzer_auto_shaders,  # Auto shader fixer operator
    fixer_operators  # New fixer operators for custom split normals and backface culling
)


bl_info = {
    "name": "Mektools",
    "author": "Meku Maki, Shino Mythmaker",
    "version": (1,2,4),
    "blender": (4,2),
    "description": "Mektools Addon Structure",
    "category": "Import-Export",
    "location": "View3D > Mektools Tab",
}

def register():
    # Register all panels
    mektools_support_community_panel.register()
    mektools_import_panel.register()
    pose_export_panel.register()
    glb_export_panel.register()
    
    # Register all operators
    import_meddle_gltf.register()
    import_textools_fbx.register()
    export_pose.register()
    export_glb.register()
    mekrig_operators.register()
    append_shaders.register()
    lizzer_auto_shaders.register()
    fixer_operators.register()  # Register the fixer operators
    

def unregister():
    # Unregister all panels
    mektools_support_community_panel.unregister()
    mektools_import_panel.unregister()
    pose_export_panel.unregister()
    glb_export_panel.unregister()
    
    # Unregister all operators
    import_meddle_gltf.unregister()
    import_textools_fbx.unregister()
    export_pose.unregister()
    export_glb.unregister()
    mekrig_operators.unregister()
    append_shaders.unregister()
    lizzer_auto_shaders.unregister()
    fixer_operators.unregister()  # Unregister the fixer operators

if __name__ == "__main__":
    register()
