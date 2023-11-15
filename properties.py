import bpy


class HelloWorldProperties(bpy.types.PropertyGroup):
    text: bpy.props.StringProperty(
        name="Text",
        description="Text and name of the object to spawn",
        default="Hello World!"
    )

    def register():
        bpy.types.Scene.hello_world = bpy.props.PointerProperty(
            type=HelloWorldProperties)
