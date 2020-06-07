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
print("samples = 50, render -- start")
bpy.context.scene.appleseed.samples = 50 # 0.5 hours
bpy.context.scene.render.filepath = 'C:/Users/boris/Desktop/Diplom/3D_Models/C_tranclucent_curtains/0_appleseed/С0_curt_50.png'
#start = time.perf_counter()
start = time.time()
bpy.ops.render.render(write_still=True) 

#end = time.perf_counter()
end = time.time()

render_times[render_engines[0]].append(end - start)
print("times array")
print(render_times)


print("samples = 100, render -- start")
bpy.context.scene.cycles.samples = 100 # 1 hours
bpy.context.scene.render.filepath = 'C:/Users/boris/Desktop/Diplom/3D_Models/C_tranclucent_curtains/0_appleseed/С0_curt_100.png'
#start = time.perf_counter()
start = time.time()
bpy.ops.render.render(write_still=True) 

#end = time.perf_counter()
end = time.time()

render_times[render_engines[0]].append(end - start)
print("times array")
print(render_times)

print("samples = 200, render -- start")
bpy.context.scene.cycles.samples = 200 # 2 hours
bpy.context.scene.render.filepath = 'C:/Users/boris/Desktop/Diplom/3D_Models/C_tranclucent_curtains//0_appleseed/С0_curt_200.png'
#start = time.perf_counter()
start = time.time()
bpy.ops.render.render(write_still=True) 

#end = time.perf_counter()
end = time.time()

render_times[render_engines[0]].append(end - start)
print("times array")
print(render_times)

print("samples = 400, render -- start")
bpy.context.scene.cycles.samples = 400 # 4 hours
bpy.context.scene.render.filepath = 'C:/Users/boris/Desktop/Diplom/3D_Models/C_tranclucent_curtains//0_appleseed/С0_curt_400.png'
#start = time.perf_counter()
start = time.time()
bpy.ops.render.render(write_still=True) 

#end = time.perf_counter()
end = time.time()

render_times[render_engines[0]].append(end - start)

print("times array")
print(render_times)
