import bpy
from .panels import (
    mektools_support_community_panel,
    mektools_import_panel,
    fixer_buttons_panel
)
from .operators import (
    import_meddle_gltf,
    import_textools_fbx,
    mekrig_operators,
    append_shaders
)

bl_info = {
    "name": "Mektools V1.0.1",
    "author": "Meku Maki",
    "version": (1, 0, 1),
    "blender": (4, 2, 0),
    "location": "View3D > Mektools Tab",
    "description": "Mektools V1.0.1 Addon Structure",
    "category": "Import-Export",
}

def register():
    # Register all panels
    mektools_support_community_panel.register()
    mektools_import_panel.register()
    fixer_buttons_panel.register()
    
    # Register all operators
    import_meddle_gltf.register()
    import_textools_fbx.register()
    mekrig_operators.register()
    append_shaders.register()

def unregister():
    # Unregister all panels
    mektools_support_community_panel.unregister()
    mektools_import_panel.unregister()
    fixer_buttons_panel.unregister()
    
    # Unregister all operators
    import_meddle_gltf.unregister()
    import_textools_fbx.unregister()
    mekrig_operators.unregister()
    append_shaders.unregister()

if __name__ == "__main__":
    register()
