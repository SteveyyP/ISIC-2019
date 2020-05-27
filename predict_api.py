"""
Created on Fri May  8 15:24:23 2020

@author: steveyyp
"""

import os
import cv2
import numpy as np
from PIL import Image
from tensorflow.keras.models import model_from_json

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


def load_ml_model():
    # Read JSON
    json_file = open('static/models/model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    # Load model from JSON
    model = model_from_json(loaded_model_json)
    # Load weights
    model.load_weights("static/models/model_weights.h5")

    return model


def preprocess_image(image):
    '''
    This is where image preprocessing goes

    Input
    image: str - path to image

    Output
    img: np.array - np.array of image ready for inference
    '''

    if image[-3:] == 'gif' or image[-3:] == 'png':
        Image.open(image).convert('RGB').save(image[:-4] + '.jpg')
        image = str(image[-3:]) + 'jpg'
    if image[-4:] == 'tiff':
        Image.open(image).convert('RGB').save(image[:-5] + '.jpg')
        image = str(image[-3:]) + 'jpg'

    # Read Image
    img = cv2.imread(image)

    # Correct Color Space
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Resize Image
    img = cv2.resize(img, (224, 224))

    # Reduce Noise + Keep Edges
    img = cv2.bilateralFilter(img, 2, 100, 100)

    # Convert to np.array and reshape for model
    img = np.array(img)
    img = img[np.newaxis, :]

    return img


def make_prediction(image, model, model_loaded=False):
    '''
    Make prediction about type of skin lesion

    Input
    image: str - path to image file
    model_loaded: bool - indicates whether the model is already loaded
    model: object - keras model

    Output
    preds: list - list of probabilities for each class
    '''

    if model_loaded is False:
        # Load model
        model = load_ml_model()
    else:
        # Set model to model
        model = model

    # Load and process image
    img = preprocess_image(image)

    # Make inference on image
    pred = model.predict(img)

    return pred


def decode_prediction(prediction):
    '''
    Decode prediction into human readable format

    Input
    prediction: list - list of probabilities of different image classes

    Output
    out: str - top class probability of image (class, label)
    '''

    classes = ['MEL', 'NV', 'BCC', 'AK', 'BKL', 'DF', 'VASC', 'SCC', 'UNK']
    labels = ['Melanoma',
              'Melanocytic nevus',
              'Basal-cell carcinoma',
              'Actinic keratosis',
              'Benign keratosis',
              'Dermatofibromas',
              'Vascular lesion',
              'Squamous-cell carcinoma',
              'Unknown']

    return classes[np.argmax(prediction)], labels[np.argmax(prediction)]


def class_description(lesion):
    '''
    Get a body of text providing information about the lesion type

    Input
    lesion: str - type of lesion
    lesion_dict: dict - dictionary that contains information about

    Output
    body: str - body of text about lesion type
    '''


if __name__ == '__main__':

    # Get current dir
    main_dir = os.path.dirname(os.path.realpath(__file__))

    # Define Image Path
    image = 'ISIC_0073252.jpg'
    image = os.path.join(main_dir, 'uploads/', image)

    # Load model
    model = load_ml_model()

    # Make prediction
    pred = make_prediction(image, model_loaded=True, model=model)

    # Print Result
    print(pred)
    print(decode_prediction(pred))
