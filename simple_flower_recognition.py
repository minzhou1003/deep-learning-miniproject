import tensorflow as tf
from tensorflow.python.framework import ops
import numpy as np
import matplotlib.pyplot as plt
import os
import math
from tensorflow import keras
import pathlib
from PIL import Image
import cv2
from sklearn.model_selection import train_test_split
from keras.models import model_from_json

def preprocess_test_data(image_paths):
    X = []
    size = 64, 64
    
    for img_path in image_paths:
        img = cv2.imread(str(img_path))
        im = cv2.resize(img,size)
        X.append(im)
    X = np.asarray(X)
    X = X/255.
    return X

def predict_using_simple_model(X):
    json_file = open('simple_model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights("simple_model.h5")
    print("Model successfully loaded from disk!")
    
    # compile and predict
    loaded_model.model.compile(optimizer=tf.train.AdamOptimizer(), 
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])
    y_pred = model.predict_classes(X)
    return y_pred

def main(image_paths):
    X = preprocess_test_data(image_paths)
    y_pred = predict_using_simple_model(X)
    class_names = {0:'rose', 1:'sunflower'}
    print(f'Predict result:{class_names[y_pred[i]]})
