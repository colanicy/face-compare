# -*- coding: utf-8 -*-
import cv2, numpy, time,os
from Lib.cv2fn import *
from Lib.facepp import API, File

take_picture()#获取人脸图片，并存入指定目录

#标准图像存储路径
storageDir = "source_pic"
if not os.path.exists(storageDir): os.mkdir(storageDir)
storageNowPicDir = "picture"
if not os.path.exists(storageNowPicDir): os.mkdir(storageNowPicDir)

API_KEY = "MT8PUbZ-OiWlYNSa4Ge72SZxua9jOpS5"
API_SECRET = "aK9SstvkPtfeEJPScLASLePc7DaCeGTt"

source_pic = "./source_pic/test.jpg"#标准图像
nowpic = "./picture/test.jpg"#需要认证的图像

api = API(API_KEY, API_SECRET)

ret = api.compare(image_file1=File(source_pic),image_file2=File(nowpic))


if(ret['confidence'] >= 90.0):
	print("***CONGRATULATIONS!!!***")
	print("***PASS!***")
else:
	print("***SORRY!!!***")
	print("***FAIL!***")