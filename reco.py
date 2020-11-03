import cv2
import os
import random

PATH = os.getcwd()+"/"
DIRS = os.listdir(PATH)

# Reading Image
def detect(IMG):
	img = cv2.imread(IMG)
	gray_scale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	# Reading HaarCascade File
	clf = cv2.CascadeClassifier("frontalface_haarcascade.xml")

	# Detecting Face
	face = clf.detectMultiScale(gray_scale, 1.1, 5)
	x, y, w, h = face[0]

	# Adding Rectangle
	image = cv2.rectangle(img, (x, y), (x+w, y+h), (255,0,0), 2)


	print(f"Photo Height Width is: {image.shape}") 
	(596, 640, 3)

	HEIGHT = image.shape[0]
	WIDTH = image.shape[1]

	print(HEIGHT, WIDTH)
	Adding Text
	font = cv2.FONT_HERSHEY_SIMPLEX
	if WIDTH > 350:
		thickness = 2
		fontScale = 1.02
	else:
		thickness = 1
		fontScale = 0.5
	COLOR = (0, 255, 0)
	place = (10, HEIGHT - 20)
	modified_image = cv2.putText(image, f"{len(face)} Faces Detected", place, font, fontScale, COLOR, thickness, cv2.LINE_AA)


ran_num = random.randint(9756,456476879785)
NAME_OF_IMAGE = PATH+"/"+f"photo_modified_detected_{str(ran_num)}.jpg"


print("Image Name: ", NAME_OF_IMAGE)
cv2.imwrite(NAME_OF_IMAGE, modified_image)
cv2.imshow("Grayed Image", modified_image)
cv2.waitKey(0)
