import bpy
import time
# import statistics


render_engines = ['APPLESEED_RENDER'] # поменять название рендера

# 'BLENDER_EEVEE', 'BLENDER_WORKBENCH', 'CYCLES', 'APPLESEED_RENDER', 'LUXCORE', 'RPR'

# Get the render engines registered through Python
registered_engine_types = bpy.types.RenderEngine.__subclasses__()

print("start rendering")
print(render_engines)


# The number of renders per engine for which we measure the render time
measurements_per_engine = 1
render_times = {}

for render_engine in render_engines:
    render_times[render_engine] = []


bpy.context.scene.render.engine = render_engines[0]

# поменять путь сохранения картинки

bpy.context.scene.render.filepath = 'C:/Users/boris/Desktop/Diplom/3D_Models/A_Glass/0_appleseed/A_time.png'
#start = time.perf_counter()
start = time.time()
bpy.ops.render.render(write_still=True) 

#end = time.perf_counter()
end = time.time()


render_times[render_engines[0]].append(end - start)
print(render_times)
