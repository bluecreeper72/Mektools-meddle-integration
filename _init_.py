# type: ignore
import bpy
from .operators import import_gltf
from .panels import import_export_panel

bl_info = {
    "name": "MekTools NOR",
    "author": "Meku Maki",
    "version": (1, 0, 0),
    "blender": (4, 2, 0),
    "location": "View3D > NOR Tab",
    "description": "A set of custom tools for Blender",
    "category": "Import-Export",
}

def register():
    import_gltf.register()
    import_export_panel.register()

def unregister():
    import_gltf.unregister()
    import_export_panel.unregister()

if __name__ == "__main__":
    register()
