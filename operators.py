import bpy
from bpy.types import Operator
from .utils import spawn_text_object


class HELLO_WORLD_OT_spawn_text_object(Operator):
    """Spawn a new "Hello World!" text object"""

    bl_label = "Spawn text"
    bl_idname = "hello_world.spawn_text_object"
    bl_options = {"REGISTER", "UNDO", "PRESET"}

    def execute(self, context: bpy.types.Context):
        context.window_manager.progress_begin(0, 100)

        spawn_text_object(context, context.scene.hello_world.text)

        context.window_manager.progress_update(100)
        context.window_manager.progress_end()

        return {"FINISHED"}
