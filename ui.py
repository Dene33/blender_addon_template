import bpy
from .operators import HELLO_WORLD_OT_spawn_text_object


class HELLO_WORLD_PT_main_panel(bpy.types.Panel):
    bl_label = "Spawn text object"
    bl_idname = "HELLO_WORLD_PT_main_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Hello World"

    def draw(self, context):
        layout = self.layout

        layout.prop(context.scene.hello_world, "text")
        layout.operator(HELLO_WORLD_OT_spawn_text_object.bl_idname)
