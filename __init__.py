import bpy
from .panels import (
    mektools_support_community_panel, 
    mektools_import_panel
)
from .operators import (
    import_meddle_gltf, 
    import_textools_fbx, 
    mekrig_operators,  # Consolidated operators for each Mekrig import
    append_shaders,
    lizzer_auto_shaders  # New file for auto shader fixing
)

bl_info = {
    "name": "MekTools V1.0.1",
    "author": "Meku Maki",
    "version": (1, 0, 1),
    "blender": (4, 2, 0),
    "location": "View3D > MekTools Tab",
    "description": "MekTools Addon Structure for character and material import adjustments",
    "category": "Import-Export",
}

def register():
    # Register all panels
    mektools_support_community_panel.register()
    mektools_import_panel.register()
    
    # Register all operators
    import_meddle_gltf.register()
    import_textools_fbx.register()
    mekrig_operators.register()  # Register all Mekrig import operators in this file
    append_shaders.register()
    lizzer_auto_shaders.register()  # Register the auto shader fixer operator

def unregister():
    # Unregister all panels
    mektools_support_community_panel.unregister()
    mektools_import_panel.unregister()
    
    # Unregister all operators
    import_meddle_gltf.unregister()
    import_textools_fbx.unregister()
    mekrig_operators.unregister()
    append_shaders.unregister()
    lizzer_auto_shaders.unregister()

if __name__ == "__main__":
    register()
