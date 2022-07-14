import cv2

def take_image(cam, counter, path="."):
    """
    Given a opencv VideoCapture object use it to take a picture and write the
    result in disk.
    """
    img_name = f"image_{counter}.png"

    return_value, image = cam.read()
    cv2.imwrite(img_name, image)

    counter += 1

    return img_name, counter

def send_message(client, message):
    """
    Given MQTT Client send a message
    """

    # Do STUFF

def load_image(img_path):
    """
    Load RGB image given path
    """
    return cv2.cvtColor(cv2.imread(img_path), cv2.COLOR_BGR2RGB)
