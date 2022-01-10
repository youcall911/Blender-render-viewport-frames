# AUTHOR Luigi
# VERSION 0.0.1
#功能：直接渲染当前viewport画面，自动命名
#cycles

import bpy
import time

'''
for area in bpy.context.screen.areas:
   if area.type == 'VIEW_3D':
       for space in area.spaces:
           if space.type == 'VIEW_3D':
               space.overlay.show_overlays=False #turn off viewport layout
               break
'''

#list = ['56','91','136'] #set the list of frame you want
OUTPUT = "C:/Users/luigi/Pictures"   # Where to save Images

#for i in list:
#bpy.context.scene.frame_set(int(i)) #jump to frame
timenow = time.strftime("%Y%m%d %H%M%S", time.localtime()) #add timemark
filepath = OUTPUT + "/" + str(timenow)
bpy.context.scene.render.filepath = filepath

bpy.ops.render.render(animation=False, write_still=True, use_viewport=False, layer='', scene='')