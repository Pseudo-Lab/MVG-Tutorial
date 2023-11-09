import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

for i in range(1, 20):
    if i < 10:
        img1 = cv.imread('scan1_train/rect_00'+str(i)+'_0_r5000.png',cv.IMREAD_GRAYSCALE)
    else:
        img1 = cv.imread('scan1_train/rect_0'+str(i)+'_0_r5000.png',cv.IMREAD_GRAYSCALE)
    if i + 1 < 10:
        img2 = cv.imread('scan1_train/rect_00'+str(i+1)+'_0_r5000.png',cv.IMREAD_GRAYSCALE)
    else:
        img2 = cv.imread('scan1_train/rect_0'+str(i+1)+'_0_r5000.png',cv.IMREAD_GRAYSCALE)

    # Initiate SIFT detector
    sift = cv.SIFT_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = sift.detectAndCompute(img1,None)
    kp2, des2 = sift.detectAndCompute(img2,None)
    # BFMatcher with default params
    bf = cv.BFMatcher()
    matches = bf.knnMatch(des1,des2,k=2)
    # Apply ratio test
    good = []
    for m,n in matches:
        if m.distance < 0.75*n.distance:
            good.append([m])
    # cv.drawMatchesKnn expects list of lists as matches.
    img3 = cv.drawMatchesKnn(img1,kp1,img2,kp2,good,None,flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
    #plt.imshow(img3),plt.show()
    cv.imwrite('output/out_'+str(i)+'_'+str(i+1)+'.png', img3)