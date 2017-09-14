# face-compare

将视频抓拍到的人脸图像，与存有的人脸图像进行比对。

![image](https://github.com/colanicy/face-compare/blob/master/facecompare.gif)

## 运行环境：

opencv 版本opencv_python-3.1.0-cp27-cp27m-win32

numpy 版本numpy-1.11.3+mkl-cp27-cp27m-win32

python 版本 Python 2.7.13

摄像头

## 准备工作

需要先到face++申请一个key，将main.py中的API_KEY和API_SECRET修改为自己的
API_KEY = "<<your key>>"
API_SECRET = "<<your secret>>"

## 操作

运行命令：cd到main文件所在目录

然后执行>python main.py

最后屏幕输出比对结果。

退出循环请按Q

注意：比对的目标文件是source_pic/test.jpg,你可以把这个文件更换为你自己的照片进行比对。
