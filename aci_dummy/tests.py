import pytesseract
import numpy as np
import cv2


def get_grayscale(image):
    """
    Take RGB image and gives back grayscale.

    Arguments
    ---------

    image : np.array
        Data cube (3D array) with the RGB image.

    Returns
    -------

    image : np.array
        2D array of image in grayscale.
    """
    return cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)


def test_text(im, ref_text):
    """
    Given a reference text value and a segment image see if text is the same
    based on OCR technology.

    Arguments
    ---------

    image : np.array
        Data cube (3D array) with the text segment from RGB image.

    ref_text : str
        Reference text to compare against.

    Returns
    -------

    ref == rec : bool
        Boolean from testing if the recovered text is equal to the reference.

    """

    corrected = np.flip(get_grayscale(im).transpose(), axis=0)
    inverted = np.invert(corrected)  # Tesseract needs black on white

    recovered = pytesseract.image_to_string(inverted, config='--psm 7')

    # Default to upper case and clean ends
    rec = recovered.upper().strip()
    ref = ref_text.upper().strip()

    return ref == rec


def test_color(im, ref_RGB, tolerance=0.1):
    """
    Given a reference RGB value and a segment image see if colors are of the
    same within a tolerance interval (default is 10%).

    Arguments
    ---------

    image : np.array
        Data cube (3D array) with the segment to test color as RGB image.

    tolerance : float
        Value from 0 to 0.2 (0 to 20%) to create tolerance margin.

    Returns
    -------

    all(positives) : bool
        Boolean from testing if all color channels are close to the reference
        value given the tolerance.
    """

    colors = np.rint(np.median(np.median(im, axis=0), axis=0))

    positives = []
    for ref, check in zip(ref_RGB, colors):
        positives.append(
             ref - ref*tolerance <= check <= ref + ref*tolerance
        )

    return all(positives)


def test_led(led_off, led_on, threshold=0.05):
    """
    Given RGB image segments, perform test to see if max value has increased
    significantly (above 5% by default).

    Arguments
    ---------

    led_off : np.array
        Data cube (3D array) with the RGB image. Segment with deactivated led.

    led_on : np.array
        Data cube (3D array) with the RGB image. Segment from activated led.

    threshold : float
        Value from 0 to 0.1 (0 to 10%) to generate detection threshold.

    Returns
    -------

    np.max(on) > test_value : bool
        Result from testing if maximum value is above threshold to detect LED
        activation.
    """
    on = get_grayscale(led_on)
    off = get_grayscale(led_off)

    # Detection threshold for led activation
    test_value = np.max(off)*threshold + np.max(off)

    return np.max(on) > test_value
