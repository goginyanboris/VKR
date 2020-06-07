import bpy
import time
# import statistics


render_engines = ['CYCLES'] # поменять название рендера

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
'''
# поменять путь сохранения картинки
print("samples = 155, render cycles -- start")
bpy.context.scene.cycles.samples = 155# 0.5 hours
bpy.context.scene.render.filepath = 'C:/Users/boris/Desktop/Diplom/3D_Models/C_tranclucent_curtains/1_Cycles/С1_curt_155.png'
#start = time.perf_counter()
start = time.time()
bpy.ops.render.render(write_still=True) 

#end = time.perf_counter()
end = time.time()

render_times[render_engines[0]].append(end - start)


print("samples = 310, render cycles -- start")
bpy.context.scene.cycles.samples = 310 # 1 hours
bpy.context.scene.render.filepath = 'C:/Users/boris/Desktop/Diplom/3D_Models/C_tranclucent_curtains/1_Cycles/С1_curt_310.png'
#start = time.perf_counter()
start = time.time()
bpy.ops.render.render(write_still=True) 

#end = time.perf_counter()
end = time.time()

render_times[render_engines[0]].append(end - start)

print("samples = 620, render cycles -- start")
bpy.context.scene.cycles.samples = 620 # 2 hours
bpy.context.scene.render.filepath = 'C:/Users/boris/Desktop/Diplom/3D_Models/C_tranclucent_curtains/1_Cycles/С1_curt_620.png'
#start = time.perf_counter()
start = time.time()
bpy.ops.render.render(write_still=True) 

#end = time.perf_counter()
end = time.time()

render_times[render_engines[0]].append(end - start)
'''
print("samples = 1237, render luxcore -- start")
bpy.context.scene.cycles.samples = 1237 # 4 hours
bpy.context.scene.render.filepath = 'C:/Users/boris/Desktop/Diplom/3D_Models/C_tranclucent_curtains/1_Cycles/С1_curt_1237.png'
#start = time.perf_counter()
start = time.time()
bpy.ops.render.render(write_still=True) 

#end = time.perf_counter()
end = time.time()

render_times[render_engines[0]].append(end - start)

print("times array")
print(render_times)
