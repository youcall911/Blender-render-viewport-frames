'''
AUTHOR Luigi
VERSION 0.0.2
功能：直接渲染特定帧viewport画面
分为三步，首先关闭 viewport overlays,第二步跳转到指定的帧，第三步渲染并自动命名。二三步为循环。最后再打开overlay
默认使用jpg，文件更小
如果需要透明背景：
请勾选“渲染属性 - 胶片 - 透明”
"输出属性 - 使用png格式，颜色：RGBA"
'''

import bpy
import time

for area in bpy.context.screen.areas:
    if area.type == 'VIEW_3D':
        for space in area.spaces:
            if space.type == 'VIEW_3D':
                space.overlay.show_overlays=False #turn off viewport layout
                break

list = ['55', '90', '125'] #set the list of frame you want
OUTPUT = "C:/Users/.../Pictures"   # Where to save Images

for i in list:
    bpy.context.scene.frame_set(int(i)) #jump to frame
    timenow = time.strftime("%Y%m%d %H%M%S", time.localtime()) #add timemark
    filepath = OUTPUT + "/" + str(timenow)
    bpy.context.scene.render.filepath = filepath
    bpy.ops.render.opengl(write_still=True, view_context=True) #render viewport
