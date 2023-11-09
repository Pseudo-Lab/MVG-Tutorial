import cv2
import numpy as np
import open3d as o3d
import math
import yaml

with open('camera_info.yaml','r') as f:
    cfg = yaml.load(f)
K_=cfg['intrinsic']
d_scale=cfg['depth_scale']
#depth_scale = 6553.0
img = cv2.imread('./images/frame000001.jpg', cv2.IMREAD_COLOR)
depth = cv2.imread('./images/depth000001.png',-1)


cv2.imshow("img",img)
cv2.imshow("depth",depth)
cv2.waitKey(0)
cv2.destroyAllWindows()

h_orin,w_orin,c_orin =img.shape

#color,depth image resize
img = cv2.resize(img, dsize=(300,170))
depth = cv2.resize(depth, dsize=(300,170))


h,w,c = img.shape

scale_val = h/h_orin
#print(scale_val)

K_[0][0] = K_[0][0]*scale_val
K_[1][1] = K_[1][1]*scale_val
K_[0][2] =K_[0][2]*scale_val
K_[1][2] = K_[1][2] *scale_val
d_scale = d_scale * scale_val
depth_conv = depth / d_scale
#print(depth_conv)
#print(K_)
K=K_
#K = [[150.0, 0, 149.8],[0.0, 150.0, 84.8],[0.0, 0.0, 1.0]]
#K = [[152.25, 0.0, 160.0],[0.0, 152.25, 120.0],[0.0, 0.0, 1.0]] # Intrinsic parameter
K = np.array(K)
K_inv =np.linalg.inv(K) # Intrinsic parameter inverse


cmap = np.empty((0,6))
cnt =0
for i in range(0,h):
    for j in range(0,w):
        #print('cnt ', cnt)
        cnt+=1
        uv=np.array([i,j,1])
        uv_depth = depth_conv[i,j]
        #print('depth is ',uv_depth)
        point=uv_depth*K_inv.dot(uv)
        RGB = img[i,j]
        #print(type(point))
        global_color = np.append(point,RGB)
        global_color=global_color.reshape(1,6)
        cmap =np.append(cmap,global_color,axis=0)
        #print('cmape',cmap.shape)
        #global_color=[global_color]
        #cmap.append(global_color)
        #print(cmap)
        #print(global_color[0])
        #print('point',global_color.shape)
        #print(global_color.shape)
        #cmap = np.append(cmap,global_color,axis=0)
        #print(cmap.shape)
        #print(type(points))
        #print('X Y Z ', X,' ',Y,' ',Z)
        #print('RGB is ',img[i,j])
        #print(depth_conv)
        #print(img[i,j]) 
#print('cmap size ',cmap.shape)
#print(cmap)

pts=cmap[0:,:3] # Global points position
colors=cmap[:,3:6]/255 # Global points' color

#print('pts ', pts)
#print('colors ',colors)

pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(pts)
pcd.colors = o3d.utility.Vector3dVector(colors)
#pcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=30))
o3d.visualization.draw_geometries([pcd],point_show_normal=False)
o3d.io.write_point_cloud("reconstruction_pcd.pcd", pcd)

