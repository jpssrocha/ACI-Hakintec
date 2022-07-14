import numpy as np
import cv2
from tests import test_led, test_color, test_text
from im_io import take_image, send_message, load_image
from termcolor import colored


def segment(image):
    '''
    Given RGB image, loaded as a 3D numpy array. Return segments based on map
    generated manually.

    Obs: This map is created based on hard coded data colected manually from
    analysing the reference images. A finished product would need a more
    elegant solution ...

    Arguments
    ---------

    image : 3D np.array
        RGB image of the board to analyse with this map.

    Returns
    -------

    segments : dict
        Dictionary with the segments and the reference values for passing
        to the tests.

    '''

    segments = {
            'relay1': {'seg': image[177:344, 32:166, :], 'ref': [38, 222, 255]},
            'relay2': {'seg': image[176:343, 178:311, :], 'ref': [1, 125, 220]},
            'relay3': {'seg': image[174:341, 323:459, :], 'ref': [255, 207, 240]},
            'relay4': {'seg': image[176:347, 471:614, :], 'ref': [26, 223, 255]},
            'LED1': {'seg': image[26:49, 273:314, :], 'ref': None},
            'LED2': {'seg': image[26:49, 330:369, :], 'ref': None},
            'LED3': {'seg': image[26:49, 385:427, :], 'ref': None},
            'LED4': {'seg': image[26:49, 439:480, :], 'ref': None},
            'texto1': {'seg': image[225:330, 577:613, :], 'ref': 'TONGLING'}
    }

    return segments


def automated_test_routine(image_file):
    '''
    Run routine of automated tests in a given image. This version only checks
    color and text (dummy_version).

    Arguments
    ---------

    image_file : str
        Path of the file

    Returns
    -------
        all(final_results) : bool
            True if all tests worked out.

    '''
    # Take first image
    # Here we should have the camera operation but for now we will only load
    # the image from disk
    first_image = load_image(image_file)
    first_map = segment(first_image)

    final_results = []

    # Test Color

    print("\n")

    print('Initializing color tests ... \n')

    to_test_color = ['relay1', 'relay2',  'relay3', 'relay4']

    test_results = []
    for component in to_test_color:
        # Make tests
        data = first_map[component]
        test = test_color(data['seg'], data['ref'])

        if test:
            print(colored(f'Component: {component}: PASSED', 'green'))
        if not test:
            print(colored(f'Component: {component}: FAILED', 'red'))

        test_results.append(test)

    print('\n')

    final_result = all(test_results)

    final_results.append(final_result)

    if final_result:
        print(colored(f'Color position test: PASSED\n', 'green'))

    if not final_result:
        print(colored(f'Color position test: FAILED\n', 'red'))

    ## Test Text

    print('Initializing text tests ... \n')

    to_test_text = ['texto1']

    test_results = []
    for component in to_test_text:
        # Make tests
        data = first_map[component]
        test = test_text(data['seg'], data['ref'])

        if test:
            print(colored(f'Component: {component}: PASSED', 'green'))
        if not test:
            print(colored(f'Component: {component}: FAILED', 'red'))

        test_results.append(test)

    print('\n')

    final_result = all(test_results)

    final_results.append(final_result)

    if final_result:
        print(colored(f'Text position test: PASSED\n', 'green'))

    if not final_result:
        print(colored(f'Text position test: FAILED\n', 'red'))

    # Test LEDS - FORGET THE LEDS FOR NOW !!!

    # to_test_led = ['led1', 'led2',  'led3', 'led4']
    # for component in to_test_led:
    #     # Do stuff
    #     pass

    return all(final_results)


if __name__ == '__main__':

    end_result = automated_test_routine("image_2.png")

    # Print final result

    if end_result:
        print(colored('DONE: ALL TESTS PASSED!', 'green'))

    if not end_result:
        print(colored('DONE: ALL OR SOME TESTS FAILED!', 'red'))

