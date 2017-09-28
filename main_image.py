# -*- coding: utf-8 -*-
import cv2, numpy, time,os
from Lib.imagepp import API, File

#API_KEY = "<<your key>>"
API_KEY = "MT8PUbZ-OiWlYNSa4Ge72SZxua9jOpS5"
#API_SECRET = "<<your secret>>"
API_SECRET = "aK9SstvkPtfeEJPScLASLePc7DaCeGTt"

source_pic = "./orc2.jpg"

api = API(API_KEY, API_SECRET)

ret = api.recognizetext(image_file=File(source_pic))

for item in ret["result"]:
	print "*************************************"
	print item
print len(ret["result"])
print ret["result"]



