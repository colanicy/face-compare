import cv2, os

API_KEY = "MT8PUbZ-OiWlYNSa4Ge72SZxua9jOpS5"
API_SECRET = "aK9SstvkPtfeEJPScLASLePc7DaCeGTt"

faceCascade = cv2.CascadeClassifier(os.path.join('Lib', 'haarcascade_frontalface_default.xml'))

def take_picture(name="test",storageDir='picture'):
    if not os.path.exists(storageDir): os.mkdir(storageDir)
    cap = cv2.VideoCapture(0)
    if not cap.isOpened(): print('Cap failed because of camera')

    print('Press **Q** to quit!')
    print('Press **Space** to take a picture!')
    while 1:
        ret, img = cap.read()
        cv2.imshow('Image',img)
        faces = detect_face(img)
        if len(faces) == 1:
                print('Face found')
        elif not faces:
            print('No face found')
        else:
            print('More than one face found')
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord(' '):
            if len(faces) == 1:
                cv2.imwrite(os.path.join(storageDir, '%s.jpg'%name), img)
                cv2.imshow('Capture Image', img)
                print('The picture tacked!!!')
    cap.release()
    cv2.destroyAllWindows()
    return os.path.join(storageDir, '%s.jpg'%name)

def detect_face(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.3, 5)
    return faces
