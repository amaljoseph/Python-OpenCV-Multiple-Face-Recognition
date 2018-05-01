import cv2
import sys

def face_detect(imagePath):	
	cascPath = "opencv-files/haarcascade_frontalface_alt.xml"
	faceCascade = cv2.CascadeClassifier(cascPath)
	image = cv2.imread(imagePath)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	grays = []
	faces = faceCascade.detectMultiScale(
		gray,
		scaleFactor=1.1,
		minNeighbors=5,
		minSize=(30, 30)
	)

	for (x, y, w, h) in faces:
		cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

	cv2.imshow("Faces found", image)
	cv2.waitKey(1)
	for i in range(0, len(faces)):
		(x, y, w, h) = faces[i]
		grays.append(gray[y:y+w, x:x+h])
	print "------------------------------------------------------------"
	print "Detecting Face -\-"
	print grays
	print "------------------------------------------------------------"
	return grays, faces, len(faces)
