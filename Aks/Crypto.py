import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten


# Step 2: Load the MNIST dataset
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Step 3: Preprocess the data
train_images = train_images.astype('float32') / 255.0
test_images = test_images.astype('float32') / 255.0
train_images = train_images.reshape((-1, 784))
test_images = test_images.reshape((-1, 784))

# Step 4: Create the neural network model
model = Sequential()
model.add(Dense(128, activation='relu', input_shape=(784,)))
model.add(Dense(64, activation='relu'))
model.add(Dense(10, activation='softmax'))

# Step 5: Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Step 6: Train the model
model.fit(train_images, train_labels, epochs=10, batch_size=32, validation_split=0.2)

# Step 7: Evaluate the model on the test set
test_loss, test_accuracy = model.evaluate(test_images, test_labels)
print(f'Test accuracy: {test_accuracy}')

# Step 8: Perform predictions on new images
# Replace 'new_image_path.png' with the path to your own handwritten digit image
new_image = tf.keras.preprocessing.image.load_img('3_Handwritten_Digit.jpg', color_mode='grayscale', target_size=(28, 28))
new_image = tf.keras.preprocessing.image.img_to_array(new_image)
new_image = new_image.reshape((1, 784)) / 255.0

prediction = model.predict(new_image)
predicted_label = np.argmax(prediction[0])
print(f'Predicted digit: {predicted_label}')