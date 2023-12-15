'''
AUTHOR Luigi
功能：直接渲染特定帧viewport画面，自动保存到我的图片
分为三步，首先关闭 viewport overlays,第二步跳转到指定的帧，第三步渲染并自动命名。二三步为循环。最后再打开overlay
默认使用jpg，文件更小
如果需要透明背景：
请勾选“渲染属性 - 胶片 - 透明”
"输出属性 - 使用png格式，颜色：RGBA"
'''

import bpy
import time
import os

'''
for area in bpy.context.screen.areas:
   if area.type == 'VIEW_3D':
      for space in area.spaces:
         if space.type == 'VIEW_3D':
            space.overlay.show_overlays=False #turn off viewport layout
           break
'''

# list = ['55', '90', '125'] #set the list of frame you want
#OUTPUT = "C:/Users/Administrator/Pictures"   # Where to save Images
OUTPUT = os.path.join(os.path.expanduser('~'), 'Pictures')  
# 自动保存到我的图片

#读取当前文件名
filename = bpy.path.basename(bpy.context.blend_data.filepath)
#删除blend后缀
filename = filename.strip('.blend')

#读取当前相机名称
cameraname = bpy.context.scene.camera.name

#for i in list:
#bpy.context.scene.frame_set(int(i)) #jump to frame
timenow = time.strftime("%Y%m%d %H%M%S", time.localtime()) 
#日期

filepath = OUTPUT + "/" + str(timenow) + ' ' + str(cameraname) + ' ' + str(filename)
#生成路径

bpy.context.scene.render.filepath = filepath
bpy.ops.render.opengl(write_still=True, view_context=True) 
#render viewport