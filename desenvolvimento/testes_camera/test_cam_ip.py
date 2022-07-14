import cv2
import matplotlib.pyplot as plt

ip = "http://192.168.0.104"
port = "4747"
cam = cv2.VideoCapture(f"{ip}:{port}/mjpegfeed")

return_value, image = cam.read()

plt.imshow(image)
