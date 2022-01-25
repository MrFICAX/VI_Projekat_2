from cv2 import VideoCapture, imwrite
import face_recognition as frec

def recognizeFaceFromCamera():
    
    cam = VideoCapture(0)
    known_faces = []
    known_faces.append(frec.face_encodings(frec.load_image_file("./known-faces/veljko.jpg"))[0])
    known_faces.append(frec.face_encodings(frec.load_image_file("./known-faces/zeljko.jpg"))[0])
    known_faces.append(frec.face_encodings(frec.load_image_file("./known-faces/filip.jpg"))[0])
    (result, img) = cam.read()
    if result:
        imwrite("myimg.jpg", img)
        myface = frec.face_encodings(frec.load_image_file("myimg.jpg"))[0]
        cpmresults = frec.compare_faces(known_faces, myface)
        for faceresult in cpmresults:
            if faceresult:
                return True
        return False
    else:
        return False

    camr= VideoCapture(0)
    res, i = camr.read()
    imwrite("./known-faces/veljko.jpg", i)

recognizeFaceFromCamera()