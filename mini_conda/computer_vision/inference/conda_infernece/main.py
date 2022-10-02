#import libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg  
import seaborn as sns
import tensorflow as tf
from tensorflow.python.framework import ops
import tensorflow_datasets as tfds
from tensorflow import keras
from PIL import Image

# Import Fashion MNIST

(train_images, train_labels), (test_images, test_labels) \
        = tf.keras.datasets.fashion_mnist.load_data()




class_names = ['T-shirt/top', 'Trouser', 
        'Pullover', 'Dress', 'Coat', 
        'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']


train_images = train_images / 255.0

test_images = test_images / 255.0


# Prepare the training images
train_images = train_images.reshape(train_images.shape[0], 28, 28, 1)

# Prepare the test images
test_images = test_images.reshape(test_images.shape[0], 28, 28, 1)



model = keras.models.load_model("fashion_mnist_model.h5")


#run test image from Fashion_MNIST data 

img = test_images[15]
img = (np.expand_dims(img,0))
singlePrediction = model.predict(img,steps=1)
print ("Prediction Output")
print(singlePrediction)
print()
NumberElement = singlePrediction.argmax()
Element = np.amax(singlePrediction)

print ("Our Network has concluded that the image number '15' is a "
        +class_names[NumberElement])
print (str(int(Element*100)) + "% Confidence Level")



