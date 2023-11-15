import bpy


def spawn_text_object(context: bpy.types.Context, text: str):
    text_curve = bpy.data.curves.new(text, "FONT")
    text_curve.body = text
    obj = bpy.data.objects.new(text, text_curve)
    context.collection.objects.link(obj)

    return obj
