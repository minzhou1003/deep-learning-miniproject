# deep-learning-mini project
This is the mini project from EC601.

Author: Min Zhou

Email: minzhou@bu.edu


## Introduction

In this mini project, I have trained two different deep learning model to recognize roses and sunflowers.

1. A simple model(without conv layer): only contains one simple flatten layer and two densely-connected NN layers.
2. [VGG-16](https://arxiv.org/pdf/1409.1556v6.pdf) model: using the VGG-16 structure.
3. Training, validation and test dataset:
```
Number of training examples = 1092
Number of validation examples = 274
Number of test examples = 152
X_train shape: (1092, 64, 64, 3)
y_train shape: (1092,)
X_val shape: (274, 64, 64, 3)
y_val shape: (274,)
```

## File Instruction
* `rose` folder: images of rose.
* `sunflower` folder: images of sunflower.
* `test_images` folder: store all the images you want to test using the trained model. There are three images already if you don't have test images.
* `flower_recognition_using_deep_learning.ipynb`: the Jupyter Notebook for developing and training the model.
* `simple_flower_recognition.py`: the python script to run the trained "simple model".
* `simple_model.h5`: trained model weights.
* `simple_model.json`: trained model.
* `vgg16_model.h5`: trained VGG-16 weights.
* `vgg16_model.json`: trained VGG-16 model.
* `requirements.txt`: necessary python libraries.


## Compare models:
The test accuracy of the simple model and VGG-16 model are 85.5% and 55.9% respectively. There are some main facts caused the lower accuracy of VGG-16 model:

1. Overfitting
    * Lack of data.
    * The model is too complex for this simple binary classification problem. 
3. Optimal hyperparameters need to be tuned in the future.

## Installation:

### 1. Download this repository:
```
git clone https://github.com/minzhou1003/deep-learning-miniproject.git
```

### 2. Put your test image to the `test_images/` folder

There are three images already if you don't have test images.

### 3. Set up and activate virtualenv inside that folder.
```
cd deep-learning-miniproject
virtualenv --python python3 env
source env/bin/activate
```

### 4. Install python libraries:
```
pip install -r requirements.txt
```

### 5. Run the python API of the simple model:
```
python simple_flower_recognition.py
```

### 6. Sample output:
```
$ python simple_flower_recognition.py
Using TensorFlow backend.

Did you put all test images to the "/test_images" folder? ("yes"/"no") yes
2018-10-22 01:33:58.746880: I tensorflow/core/platform/cpu_feature_guard.cc:141] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA

Model successfully loaded from disk!

Image: 15951588433_c0713cbfc6_m.jpg, Predict result: rose

Image: 15965652160_de91389965_m.jpg, Predict result: rose

Image: 15972975956_9a770ca9dd_n.jpg, Predict result: sunflower
```


## Goals:
1. [x] Use TensorFlow (or any tool you prefer) to recognize between two classes of objects.
* [x] Roses and Sunflowers
2. [x] You need to capture the images yourself and tag them.  You can use any Tagging system (e.g, https://hubs.ly/H0dktLv0 Neurala).  
3. [x] You need to design your own Training, Testing, and Verification sets.
4. [x] You need to compare between two different systems based on the literature review you did and/or reading the material provided
Bonus:  Provide an API with example code for another developer to use your system
