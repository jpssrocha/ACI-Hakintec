import pytesseract
import numpy as np
import cv2

def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

def test_text(im, ref_text):
    """
    Given a reference text value and a segment 
    image see if text is the same based on
    OCR technology.
    """ 
    corrected = np.flip(get_grayscale(im).transpose(), axis=0)
    inverted = np.invert(corrected)  # Tesseract needs black on white
    
    recovered = pytesseract.image_to_string(inverted, config='--psm 7')
    
    
    # Default to upper case and clean ends
    rec = recovered.upper().strip()
    ref = ref_text.upper().strip()
    
    return ref == rec


def test_color(im, ref_RGB, tolerance = 0.1):
    """
    Given a reference RGB value and a segment 
    image see if colors areo f the same within 
    a confidence interval (default is 10%).
    """
    
    colors = np.rint(np.median(np.median(im, axis=0), axis=0))
    
    positives = []
    for ref, check in zip(ref_RGB, colors):
        positives.append(
             ref - ref*tolerance <= check <= ref + ref*tolerance
        )
    
    return all(positives)


def test_led(led_off, led_on, tolerance = 0.05):
    """
    Given RGB image segments, perform test to see if 
    max value has increased significantly (above 5%
    by default)
    """
    on = get_grayscale(led_on)
    off = get_grayscale(led_off)

    test_value = np.max(off)*tolerance + np.max(off)

    return np.max(on) > test_value
