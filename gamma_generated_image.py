import os
import re
import shutil
import cv2
import numpy as np 
import shutil

def adjust_gamma(image , gamma = 1.0):
	invgamma = 1 / gamma
	table = np.array([ ((i / 255.0 )**invgamma)*255 for i in np.arange(0,256)]).astype("uint8")
 	
	return cv2.LUT(image, table)

def get_image(input_img, xml,glb):
	original =cv2.imread(input_img,1)
	gamma_dir = os.path.join(os.getcwd(),'Gamma')
	for gamma in np.arange(0.0, 3.5, 3.0):
	    if gamma == 1:
	        continue
	    gamma = gamma if gamma > 0 else 0.5
	    adjusted = adjust_gamma(original, gamma=gamma)
	    cv2.putText(adjusted, "g={}".format(gamma), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
	    cv2.imwrite(gamma_dir+"/"+'img'+str(gamma)+str(glb)+'.jpg', adjusted)
	    shutil.copy(xml, gamma_dir+"/"+'img'+str(gamma)+str(glb)+'.xml')
	return 0;

def main():
	glb = 1
	files = os.listdir()
	images = [img.split(".")[0] for img in files if img[-3:] == 'jpg']
	length = int(np.floor(len(images)))
	file_pair = [(img+".jpg",img+".xml") for img in images]
	image_directory = os.getcwd()
	for pair in file_pair:
		glb+=6
		get_image(image_directory+"/"+pair[0],image_directory+"/"+pair[1],glb)

main()
