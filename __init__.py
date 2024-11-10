import bpy
from .panels import (
    mektools_support_community_panel, 
    mektools_import_panel,
    mythtools_export_panel
)
from .operators import (
    import_meddle_gltf, 
    import_textools_fbx, 
    export_pose,       #.pose file export 
    mekrig_operators,  # Consolidated operators for each Mekrig import
    append_shaders,
    lizzer_auto_shaders,  # Auto shader fixer operator
    fixer_operators  # New fixer operators for custom split normals and backface culling
)

bl_info = {
    "name": "MekTools V1.0.2",
    "author": "Meku Maki, Shino Mythmaker",
    "version": (1, 0, 2),
    "blender": (4, 2, 0),
    "location": "View3D > MekTools Tab",
    "description": "MekTools Addon Structure for character and material import adjustments",
    "category": "Import-Export",
}

def register():
    # Register all panels
    mektools_support_community_panel.register()
    mektools_import_panel.register()
    mythtools_export_panel.register()
    
    # Register all operators
    import_meddle_gltf.register()
    import_textools_fbx.register()
    export_pose.register()
    mekrig_operators.register()
    append_shaders.register()
    lizzer_auto_shaders.register()
    fixer_operators.register()  # Register the fixer operators

def unregister():
    # Unregister all panels
    mektools_support_community_panel.unregister()
    mektools_import_panel.unregister()
    mythtools_export_panel.unregister()
    
    # Unregister all operators
    import_meddle_gltf.unregister()
    import_textools_fbx.unregister()
    export_pose.unregister()
    mekrig_operators.unregister()
    append_shaders.unregister()
    lizzer_auto_shaders.unregister()
    fixer_operators.unregister()  # Unregister the fixer operators

if __name__ == "__main__":
    register()
