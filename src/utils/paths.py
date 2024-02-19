import os

PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../'))
ASPECT_EXTRACTOR_PATH = os.path.join(PROJECT_PATH, 'aspect_extractor')
ASPECT_EXTRACTOR_WEIGHTS_PATH = os.path.join(ASPECT_EXTRACTOR_PATH, 'weights', 'weights.h5')