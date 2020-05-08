import bpy
import time
# import statistics

render_engines = ['APPLESEED_RENDER'] # поменять название рендера !!!!!!!!!!!

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

# поменять путь сохранения картинки !!!!!!!!!!!!
bpy.context.scene.appleseed.renderer_passes = 23 # 30 min
bpy.context.scene.render.filepath = 'C:/Users/boris/Desktop/Diplom/3D_Models/A_Glass/0_appleseed/A_23_samp.png'

start = time.time()
bpy.ops.render.render(write_still=True) 
end = time.time()
print("23", render_times)

# поменять путь сохранения картинки !!!!!!!!!!!!
bpy.context.scene.appleseed.renderer_passes = 46# 1 hour
bpy.context.scene.render.filepath = 'C:/Users/boris/Desktop/Diplom/3D_Models/A_Glass/0_appleseed/A_46_samp.png'

start = time.time()
bpy.ops.render.render(write_still=True) 
end = time.time()
print("46", render_times)

# поменять путь сохранения картинки !!!!!!!!!!!!
bpy.context.scene.appleseed.renderer_passes = 92 # 2 hours
bpy.context.scene.render.filepath = 'C:/Users/boris/Desktop/Diplom/3D_Models/A_Glass/0_appleseed/A_92_samp.png'

start = time.time()
bpy.ops.render.render(write_still=True) 
end = time.time()
print("92", render_times)

# поменять путь сохранения картинки !!!!!!!!!!!!
bpy.context.scene.appleseed.renderer_passes = 184 # 4 hours
bpy.context.scene.render.filepath = 'C:/Users/boris/Desktop/Diplom/3D_Models/A_Glass/0_appleseed/A_184_smp.png'

start = time.time()
bpy.ops.render.render(write_still=True) 
end = time.time()

render_times[render_engines[0]].append(end - start)
print(render_times)
