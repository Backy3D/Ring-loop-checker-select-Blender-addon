bl_info = {
    "name": "Ring loop checker select",
    "author": "Backy3D",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > UI",
    "description": "Checker selects a cylinder with ring loops",
    "warning": "",
    "doc_url": "https://github.com/Backy3D/Ring-loop-chequer-select",
    "category": "Mesh",
}




import bpy
import bpy
from bpy.types import (
    AddonPreferences,
    Operator,
    Panel,
    PropertyGroup
)


def main(context):
    for ob in context.scene.objects:
        print(ob)


class SimpleOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "mesh.simple_operator"
    bl_label = "Ring loop checker select"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None
    
    def execute(self, context):
        iterations = 1
        main(context)
        bpy.ops.mesh.loop_multi_select(ring=True)
        bpy.ops.mesh.select_nth(nth = iterations)
        bpy.ops.mesh.loop_multi_select(ring=False)

        return {'FINISHED'}


def menu_func(self, context):
    self.layout.operator(SimpleOperator.bl_idname, text=SimpleOperator.bl_label)


def register():
    bpy.utils.register_class(SimpleOperator)
    bpy.types.VIEW3D_MT_select_edit_mesh.append(menu_func)


def unregister():
    bpy.utils.unregister_class(SimpleOperator)
    bpy.types.VIEW3D_MT_select_edit_mesh.remove(menu_func)
    

if __name__ == "__main__":
    register()

    # test call
    #bpy.ops.mesh.simple_operator()
