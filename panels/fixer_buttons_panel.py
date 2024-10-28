import bpy
from bpy.types import Panel, Operator

class VIEW3D_PT_FixerButtons(Panel):
    """Fixer Buttons Panel for Manual Import Operations"""
    bl_label = "Fixer Buttons"
    bl_idname = "VIEW3D_PT_fixer_buttons"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Mektools'

    def draw(self, context):
        layout = self.layout

        # Description text
        layout.label(text="Use these when manually importing characters.")

        # Clear Parents button
        layout.operator("mektools.clear_parents", text="Clear Parents")

class MEKTOOLS_OT_ClearParents(Operator):
    """Clear Parent Keep Transforms on selected objects"""
    bl_idname = "mektools.clear_parents"
    bl_label = "Clear Parents (Keep Transforms)"

    def execute(self, context):
        # Run Blender's internal Clear Parent Keep Transform operation
        bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM')
        self.report({'INFO'}, "Cleared parents and kept transforms for selected objects.")
        return {'FINISHED'}

def register():
    bpy.utils.register_class(VIEW3D_PT_FixerButtons)
    bpy.utils.register_class(MEKTOOLS_OT_ClearParents)

def unregister():
    bpy.utils.unregister_class(VIEW3D_PT_FixerButtons)
    bpy.utils.unregister_class(MEKTOOLS_OT_ClearParents)
