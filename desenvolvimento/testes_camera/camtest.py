import cv2

cam = cv2.VideoCapture(1)
img_counter = 0

def take_image(cam, counter, path="."):
    """
    Given a opencv VideoCapture object use it to take a picture and write
    the result in disk.
    """
    img_name = f"image_{counter}.png"

    return_value, image = cam.read()
    cv2.imwrite(img_name, image)

    counter += 1

    return img_name, counter

image, img_counter = take_image(cam, img_counter)

print(image, img_counter)
    

cam.release()
