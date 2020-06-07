import bpy
import time
import numpy as np

 # поменять название рендера !!!!!!!!!!!

# 'BLENDER_EEVEE', 'BLENDER_WORKBENCH', 'CYCLES', 'APPLESEED_RENDER', 'LUXCORE', 'RPR'

# Get the render engines registered through Python
registered_engine_types = bpy.types.RenderEngine.__subclasses__()

print('start rendering')


bpy.context.scene.render.engine = 'LUXCORE'

# 'BLENDER_EEVEE', 'BLENDER_WORKBENCH', 'CYCLES', 'APPLESEED_RENDER', 'LUXCORE', 'RPR'

# поменять путь сохранения картинки !!!!!!!!!!!!
# bpy.context.scene.appleseed.threads = 1    # количество потоков

bpy.context.scene.luxcore.halt.samples = 88  # 1 hour
bpy.context.scene.render.filepath = 'C:/Users/UserPushka/Desktop/Diplom/3D_Models/B_Bottles/2_LuxCore/B2_88_6tr.png'

render_meanTime = []
render_varTime = []

t=[]
for i in range(1):

    start = time.time()
    bpy.ops.render.render(write_still=True) 
    end = time.time()
    t.append(end - start)

render_meanTime.append(np.mean(t))
render_varTime.append(np.var(t))

print('mean time =', render_meanTime[0])



bpy.context.scene.luxcore.halt.samples = 173 # 10 min
bpy.context.scene.render.filepath = 'C:/Users/UserPushka/Desktop/Diplom/3D_Models/B_Bottles/2_LuxCore/B2_173_6tr.png'

t=[]
for i in range(1):
    
    start = time.time()
    bpy.ops.render.render(write_still=True) 
    end = time.time()
    t.append(end - start)

render_meanTime.append(np.mean(t))
render_varTime.append(np.var(t))




bpy.context.scene.luxcore.halt.samples = 335     # 30 min
bpy.context.scene.render.filepath = 'C:/Users/UserPushka/Desktop/Diplom/3D_Models/B_Bottles/2_LuxCore/B2_335_6tr.png'

t=[]
for i in range(1):
    
    start = time.time()
    bpy.ops.render.render(write_still=True) 
    end = time.time()
    t.append(end - start)

render_meanTime.append(np.mean(t))
render_varTime.append(np.var(t))




bpy.context.scene.luxcore.halt.samples = 676  # 10 min
bpy.context.scene.render.filepath = 'C:/Users/UserPushka/Desktop/Diplom/3D_Models/B_Bottles/2_LuxCore/B2_676_6tr.png'

t=[]
for i in range(1):
    
    start = time.time()
    bpy.ops.render.render(write_still=True) 
    end = time.time()
    t.append(end - start)

render_meanTime.append(np.mean(t))
render_varTime.append(np.var(t))



print('\nmean time =', render_meanTime, '\n\nsec_var=', render_varTime)