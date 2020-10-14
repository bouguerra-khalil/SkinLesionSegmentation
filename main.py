import cv2 as cv
import numpy as np
import math
import os
from matplotlib import pyplot as plt
from hair_removal import hair_removal	
from untils import viewImage,contour,apply_contours
from metrics  import compare_2_segmentation,get_metrics,get_best_channel,get_graphs_channel
from color_space_transform import color_space_trans
from filter import generate_kernal,apply_filter
from Intensity_Adjustment import Histo,PlotHisto,Intensity_Adjustment,Range,imadjust
from otsu_threshold import otsu_threshold
from Connected_Components import valid , bfs, merge, cluster 


all_channels = ['R','G','B','X','Y','Z','S','I','H']
images=[4] #Put the list of images names here   

for name in images:
	for channel in all_channels[:3]:
	    img = cv.imread('images/'+str(name)+'.jpg',1)
	    img = cv.resize(img,(1024,800))
	    img_no_hair = air_removal(img)
	    print("Executing on Channel : " + channel)
	    img = color_space_trans(img_no_hair,channel)
	    print()
	    cv.imwrite("out/"+str(name)+"_"+channel+"_orignal.jpg",img)
	    kernal=generate_kernal(2)
	    img=apply_filter(img,kernal)
	    img2=np.asarray(img)
	    cv.imwrite("out/"+str(name)+"_"+channel+"1D.jpg",img2)
	    img_adjusted=imadjust(img2,img2.min(),img2.max(),0,1) 
	    viewImage(img_adjusted,"adjested "+ channel)
	    cv.imwrite("out/"+str(name)+"_"+channel+"_histo.jpg",img_adjusted)


path ='./data/melanoma/'
metrics_matrix=[]
def get_results(path): 
    for subdir, dirs, files in os.walk(path):
        if(dirs==[]):
            image_name=subdir.split('/')[-1]
            gt_seg_file_name=subdir+"/"+image_name+"_Segmentation.png"
            seg_gt=cv.imread(gt_seg_file_name,cv.IMREAD_GRAYSCALE)
            row=[]
            for file in files:
                if(subdir+'/'+file==gt_seg_file_name):
                    continue
                img=cv.imread(subdir+'/'+file,cv.IMREAD_GRAYSCALE)
                row.append(get_metrics(img,seg_gt))
            metrics_matrix.append(row)

get_results(path)
print(metrics_matrix)

img1=cv.imread('./data/ISIC/results/ISIC_0000019/XoYoR.png',cv.IMREAD_GRAYSCALE)
img2=cv.imread('./data/ISIC/results/ISIC_0000019/I.png',cv.IMREAD_GRAYSCALE)
img3=cv.imread('./data/ISIC/results/ISIC_0000019/RGBoRoGoB.png',cv.IMREAD_GRAYSCALE)
img4=cv.imread('./data/ISIC/results/ISIC_0000019/RoG.png',cv.IMREAD_GRAYSCALE)
img=cv.imread('./data/ISIC/results/ISIC_0000019.jpg',cv.IMREAD_GRAYSCALE)
img5=cv.imread('./data/ISIC/ISIC_0000019/ISIC_0000019_segmentation.png',cv.IMREAD_GRAYSCALE)
apply_contours(img,img1,img2,img3,img4,img5)
