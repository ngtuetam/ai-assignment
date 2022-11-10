import cv2 as cv
import numpy as np
import glob


def convert_to_gray(img):
    gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    return gray_img

def convert_to_bin(img):
    rows, cols, depths = img.shape
    for r in range (rows):
        for c in range (cols):
            if img[r][c][0] > 100:
                img[r][c] = 1
            else:
                img[r][c] = 0
    return img

def convert_bw(src):
    converted_image = np.zeros((src.shape))
    converted_image = 255 - src
    rows,cols = converted_image.shape
    for r in range (rows):
        for c in range (cols):
            if converted_image[r][c] > 30:
                converted_image[r][c] = 255
    return converted_image

def get_data(datapath):
    images = []
    for im in glob.glob(datapath):
        img = cv.imread(im)
        images.append(img)
    return images
    
if __name__ == "__main__":
    list_img = get_data("/home/ngtuetam/workspace/ai_assign/rgb_dataset/strawberry_rgb/*.jpg")
    bin_imgs = []
    for i in range(10):
        img = list_img[i]
        bin_imgs.append(convert_to_gray(img))
        bin_imgs[i] = convert_bw(bin_imgs[i])
        cv.imwrite(f"/home/ngtuetam/workspace/ai_assign/bin_imgs/strawberry_bin/image_{i}.jpg",bin_imgs[i])
