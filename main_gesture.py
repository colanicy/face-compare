#-*-coding:utf-8-*-

#通过Opencv获取手势，然后识别手势

import cv2
import sys
import time
from Lib.humanbodypp import API,File

camID = 0

capture = cv2.VideoCapture(camID)
cv2.namedWindow("camera",1)

if not capture.isOpened():
	print("Camera open failed!")
	print("Please inspect your camera deviceID %d."%camID)
	sys.exit()

#set FRAME_WIDTH,FRAME_HEIGHT
'''
设置摄像机分辨率的问题。
最小分辨率，宽度为4，高度为3。
以此类推应该为4的倍数或3的倍数。
你可以通过videocapture成员函数set来设置，摄像机的分辨率。
videocapture默认的情况下为640×480。
'''
FRAME_WIDTH = 640
FRAME_HEIGHT = 480
if capture.set(3,FRAME_WIDTH) and capture.set(4,FRAME_HEIGHT):
	print "Frame resize successful!"
else:
	print "Frame resize failed!"

class Rectangle:
	topLeft=(326,0)
	downRight=(640,350)
	color=(170,170,0)
	thickness=3
	lineType=7

	def __init__(self,topLeft = (0,0),downRight = (0,0),bgrcolor = (0,0,255),thickness = 3,lineType = 8):
		if topLeft :
			self.topLeft = topLeft
		if downRight:
			self.downRight = downRight
		if bgrcolor:
			self.color = bgrcolor
		if thickness:
			self.thickness = thickness
		if lineType:
			self.lineType = lineType
	def area(self):
		return (self.downRight[0] - self.topLeft[0]) * (self.downRight[1] - self.topLeft[1])

start_time = time.time()
while(True):
	ha,img = capture.read()
	end_time = time.time()
	rec = Rectangle((326,0),(640,350),(170,170,0),3,8)
	cv2.rectangle(img,rec.topLeft,rec.downRight,
		rec.color,rec.thickness,rec.lineType)
	cv2.putText(img,str(int((5-(end_time- start_time)))), (100,100), cv2.FONT_HERSHEY_SIMPLEX, 2, 255)
	cv2.imshow("camera",img)
	if(end_time-start_time>5):
            break
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

ha,img = capture.read()
capture.release()
gestureImg = img[0:300,326:640]

cv2.imwrite("wif.jpg",gestureImg)
cv2.namedWindow("gesture",cv2.WINDOW_NORMAL)

#手势识别
key = "<<your key>>"
secret = "<<your secret>>"
api = API(key, secret)

gesture = api.gesture(image_file = File("wif.jpg"))

#根据识别结果，将识别框画到图片上，并进行显示
if len(gesture["hands"])>0:
	print "Detected valid gesture!"
else:
	print "Detecte failed! %d"%len(gesture["hands"])
	sys.exit()
rec_areas = []
for  i in xrange(0,len(gesture["hands"])):
	hand_rectangle = gesture["hands"][i]["hand_rectangle"]
	rec = Rectangle((hand_rectangle["left"],hand_rectangle["top"]),
		(hand_rectangle["left"]+hand_rectangle["width"],
		hand_rectangle["top"]+hand_rectangle["height"]),
		(170,170,0), 2, 5)

	rec_areas.append(rec.area())

	cv2.rectangle(gestureImg,rec.topLeft,rec.downRight,
		rec.color,rec.thickness,rec.lineType)
	
cv2.imshow("gesture",gestureImg)
cv2.imwrite("wif.jpg",gestureImg)
#挑选面积最大的矩形
recid = rec_areas.index(max(rec_areas))
print max(gesture["hands"][recid]["gesture"],key=gesture["hands"][recid]["gesture"].get)

cv2.waitKey(0)

cv2.destroyAllWindows()
