# -*- coding: utf-8 -*-

import time
import picamera

def capture_image(camera):
    camera.resolution = (1024, 768)
    camera.start_preview()
    time.sleep(2)
    time_name = str(int(time.time()))
    camera.capture(time_name + '.jpg')


def main():
    with picamera.PiCamera() as camera:
        capture_image(camera)
   

if __name__ == '__main__':
    main()
