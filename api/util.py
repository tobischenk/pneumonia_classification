import base64
import io
import os
from pathlib import Path

import cv2
import numpy as np
import tensorflow as tf
from PIL import Image

ROOT_DIR = Path(__file__).resolve().parent.parent

model_path = os.path.join(ROOT_DIR, "models/final_model.h5")
model = tf.keras.models.load_model(model_path)


def read_b64(base64_string: str):
    # read decoded base64 into a bytes buffer
    bytes_buffer = io.BytesIO()
    bytes_buffer.write(base64.b64decode(base64_string.split(',')[0]))
    # get Image from bytes
    pimg = Image.open(bytes_buffer)
    # convert color and return image
    return cv2.cvtColor(np.array(pimg), cv2.COLOR_RGB2BGR)


def resize_and_scale_img(img):
    # resize Image to fit trained model img_size parameters
    img = cv2.resize(img, (150, 150))
    # normalize img data the same way it was done for training the model
    return img / 255


def get_prediction(img_data: np.array):
    # Read cv2 image from base64 string
    img = read_b64(img_data)
    img = resize_and_scale_img(img)

    # predict probability with loaded model
    prediction = model.predict(np.expand_dims(img, axis=0))
    # return prediction
    return prediction[0][0]
