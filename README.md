# Multiple Face Recogniton using Python & OpenCV
OpenCV based face recognition system that can detect and recognize multiple faces in an image. This project is based on this, which had only single face detection. I have implemented a multiple face system.



There are 2 parts in a face recognition system.
  1. Face Detection - To detect faces in images.
  2. Face Recognition - To recognize face of  persons in the images.
  
## 1. Face Detection.
Face detection is acheived in this project using Haar Cascade classifier. It could be used for object detection. Here we are using it for detecting faces. The algorithm is trained by feeding it lots of images with face and without faces. The algorithm extracts features from these images. Features are nothing but 

## 2. Face Recognition
We are using LBPH classifier to recognize the faces from the images. 
