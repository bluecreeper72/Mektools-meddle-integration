# type: ignore
import bpy
from .operators import import_gltf, import_fbx, append_collection, append_shaders, import_mekrig
from .panels import import_export_panel, import_mekrig_panel  # New import for the Import Mekrig panel

bl_info = {
    "name": "MekTools NOR",
    "author": "Meku Maki",
    "version": (1, 2, 0),
    "blender": (4, 2, 0),
    "location": "View3D > NOR Tab",
    "description": "A set of custom tools for Blender, including GLTF/FBX import, race-specific collection appending, and shader import",
    "category": "Import-Export",
}

def register():
    import_gltf.register()
    import_fbx.register()
    append_collection.register()
    append_shaders.register()
    import_mekrig.register()  # Register new operators for gender and race selection
    import_export_panel.register()
    import_mekrig_panel.register()  # Register new panel for Import Mekrig

def unregister():
    import_gltf.unregister()
    import_fbx.unregister()
    append_collection.unregister()
    append_shaders.unregister()
    import_mekrig.unregister()  # Unregister new operators for gender and race selection
    import_export_panel.unregister()
    import_mekrig_panel.unregister()  # Unregister new panel for Import Mekrig

if __name__ == "__main__":
    register()
