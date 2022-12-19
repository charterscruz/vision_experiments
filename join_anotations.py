import os
import cv2

# I am assuming that there are 3 annotated ojects in the original image.
# define the location of the folder containing the images
folder_path = '/media/cruz/data/datasets/marsyn/Annotations1/Annotations1/'

# Define the annotation name. The full name is composed of 3 parts: 
#   1 is a prefix depending on the original image name. I'll call it imgname
imgname = 'Image00122'
# There should be a mechanism in the script to list all images in the folder 
# (example: to know that in Annotations1 folder there annotation until Image 1000)
# then, create a cycle to go through all of those images


#   2 depends on the class of object. I'll call it objclass
objclass = 'boat'
# just like in the previous point, in here there should be a mechanism in the script
#  to list all classes for a image

#   3 depends on the index of the particular class. I'll call it objidx
# for an image and for a class get all the indexes available and 
#  interate (create a cycle) over those


annotation_name_prefix = imgname + '_' + objclass + '_'

# load each of the annotated images. This should be done in a cycle and not manually
#try:
img1_annot0 = cv2.imread(folder_path + annotation_name_prefix + '0' + '.png')
img1_annot1 = cv2.imread(folder_path + annotation_name_prefix + '1' + '.png')
img1_annot2 = cv2.imread(folder_path + annotation_name_prefix + '2' + '.png')

cv2.namedWindow('0', cv2.WINDOW_AUTOSIZE)
cv2.namedWindow('1', cv2.WINDOW_AUTOSIZE)
cv2.namedWindow('2', cv2.WINDOW_AUTOSIZE)
cv2.namedWindow('merged_annot', cv2.WINDOW_AUTOSIZE)

cv2.imshow('0', img1_annot2)
cv2.imshow('1', img1_annot0)
cv2.imshow('2', img1_annot1)

cv2.waitKey(0)

img1_semanticseg = img1_annot0 | img1_annot1 | img1_annot2

cv2.imshow('merged_annot', img1_semanticseg)
cv2.waitKey(0)