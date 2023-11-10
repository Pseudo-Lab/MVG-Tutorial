import cv2
import numpy as np
import os

def find_similar_features(image_folder_path):
    image_list = os.listdir(image_folder_path)
    num_images_to_process = 10 # 처리할 이미지 수
    subset_image_paths = [image_folder_path + file for file in image_list[:num_images_to_process]]
    matches = process_images(subset_image_paths)
    return matches

def process_images(image_paths):
    sift = cv2.SIFT_create()
    
    all_images = []
    all_keypoints = []
    all_descriptors = []

    sift = cv2.SIFT_create()
    bf = cv2.BFMatcher()

    for image_path in image_paths:
        image = cv2.imread(image_path)
        all_images.append(image)
        keypoints, descriptors = sift.detectAndCompute(image, None)
        all_keypoints.append(keypoints)
        all_descriptors.append(descriptors)

    matches = {}
    for i, (kp1, des1) in enumerate(zip(all_keypoints, all_descriptors)):
        for j, (kp2, des2) in enumerate(zip(all_keypoints, all_descriptors)):
            if i < j:
                match = bf.knnMatch(des1, des2, k=2)
                good = []
                for m, n in match:
                    if m.distance < 0.75 * n.distance:
                        good.append(m)
                matches[(i, j)] = good
                
    return matches, all_images, all_keypoints, all_descriptors

def get_camera_intrinsic_matrix(images):
    fx = images[0].shape[1]
    fy = images[0].shape[0] 
    cx = images[0].shape[1] / 2 
    cy = images[0].shape[0] / 2 
    K = np.array([[fx, 0, cx],
                [0, fy, cy],
                [0, 0, 1]])
    return K

def compute_camera_matrix(matches_dict, K):
    camera_matrices = []
    for (i, j), good_matches in matches_dict.items():
        kp1 = all_keypoints[i]
        kp2 = all_keypoints[j]
        
        src_pts = np.float32([kp1[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
        dst_pts = np.float32([kp2[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)

        E, mask = cv2.findEssentialMat(src_pts, dst_pts, K, method=cv2.RANSAC, prob=0.999, threshold=1.0)

        _, R, t, _ = cv2.recoverPose(E, src_pts, dst_pts, K)

        M = np.hstack((R, t)) # camera extrinsic matrix
        camera_matrices.append(np.dot(K, M))

    return camera_matrices

if __name__ == "__main__":
    image_folder_path = '../scan1_train'
    matches_dict, all_images, all_keypoints, all_descriptors = find_similar_features(image_folder_path)
    K = get_camera_intrinsic_matrix(all_images)
    camera_matrices = compute_camera_matrix(matches_dict, K)
