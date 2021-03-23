from cv2 import *
# initialize the camera

cam = VideoCapture(0)   # 0 -> index of camera


def photo(fn):

    s, img = cam.read()
    imwrite(fn,img)


