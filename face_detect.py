import cv2
import sys

def face_detect(imagePath):
	# HaarCascade file, to detect the face.
	faceCascade = cv2.CascadeClassifier("opencv-files/haarcascade_frontalface_alt.xml")
	image = cv2.imread(imagePath)
	#Convert image to grayscale
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	grays = []
	faces = faceCascade.detectMultiScale(
		gray,
		scaleFactor=1.1,
		minNeighbors=5,
		minSize=(30, 30)
	)
	
	# For drawing rectangles over multiple faces in the image
	for (x, y, w, h) in faces:
		cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
	
	# Show Detected faces.
	cv2.imshow("Faces found", image)
	cv2.waitKey(1)
	
	# Append the detected faces into grays list.
	for i in range(0, len(faces)):
		(x, y, w, h) = faces[i]
		grays.append(gray[y:y+w, x:x+h])
	print "------------------------------------------------------------"
	print "Detecting Face -\-"
	return grays, faces, len(faces)
