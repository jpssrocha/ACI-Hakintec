import cv2


def take_image(cam, counter, path="."):
    """
    Given a opencv VideoCapture object use it to take a picture and write the
    result in disk.

    Arguments
    ---------

    cam : cs2.VideoCapture
        VideoCapture object initialized with the camera to be used.

    counter : int
        Image count number to generate file name.

    path : str
        Path for saving the image.

    Returns
    -------

    img_name : str
        File path of the created file.

    counter : int
        Updated counter

    """
    img_name = f"{path}/image_{counter}.png"

    return_value, image = cam.read()
    cv2.imwrite(img_name, image)

    counter += 1

    return img_name, counter

def send_message(client, message):
    """
    Given MQTT Client send a message
    """
    raise NotImplementedError


def load_image(img_path):
    """
    Load RGB image given path.

    Arguments
    ---------

    img_path : str
        Path to the image.

    Returns
    -------

    image : np.array
        data cube with the RGB image.

    """
    return cv2.cvtColor(cv2.imread(img_path), cv2.COLOR_BGR2RGB)
