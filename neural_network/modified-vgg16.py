from keras.applications.vgg16 import VGG16
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
from keras.callbacks import History
from keras.callbacks import ModelCheckpoint
from keras.layers import Input, Flatten, Dense, Dropout
from keras.models import Model
from keras.preprocessing.image import ImageDataGenerator
import numpy as np
import keras.optimizers
import matplotlib.pyplot as plt

# fix random seed for reproducibility
seed = 4
np.random.seed(seed)

# train dataset size
train_dataset = 3000

# testing dataset size
test_dataset = 1200

# Generate a model with all layers (with top)
vgg16 = VGG16(weights='imagenet', include_top=True)

# fix the weights of the original network
for layer in vgg16.layers:
    layer.trainable = False

# add a dense layer
x = Dense(256, activation='relu', name='denselast')(vgg16.layers[-4].output)

# add a dropout layer
y = Dropout(0.6)(x)

# Add a layer where input is the output of the  second last layer 
predictions = Dense(3, activation='softmax', name='predictions')(y)

# Then create the corresponding model 
my_model = Model(input=vgg16.input, output=predictions)
my_model.summary()

# load weights
#my_model.load_weights("weights_best_dense.hdf5")

#compile the model
opt = keras.optimizers.Adam(lr=0.00001, beta_1=0.9, beta_2=0.999, epsilon=1e-07, decay=0.001)
my_model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])
#my_model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])

#checkpoint
filepath = "weights_best_dense_fixed2.hdf5"
checkpoint = ModelCheckpoint(filepath, monitor='val_acc', verbose=1, save_best_only=True, mode='max')

#generators
batch_size = 16
train_datagen = ImageDataGenerator(
        rescale = 1./255,
        #horizontal_flip = True,
        data_format = 'channels_last')

test_datagen = ImageDataGenerator(
        rescale = 1./255,
        #horizontal_flip = True,
        data_format = 'channels_last')
        
train_generator = train_datagen.flow_from_directory(
        r'data/train', #djd
        target_size = (224, 224),
        batch_size = batch_size,
        class_mode = 'categorical')
        
validation_generator = test_datagen.flow_from_directory(
        r'data/validation', #djd
        target_size = (224, 224),
        batch_size = batch_size,
        class_mode = 'categorical')

history = History()
callbacks_list = [checkpoint, history]
        
hist = my_model.fit_generator(
            train_generator,
            steps_per_epoch = train_dataset // batch_size,
            epochs = 30,
            callbacks = callbacks_list,
            validation_data = validation_generator,
            validation_steps = test_dataset // batch_size)

# summarize history for accuracy
plt.plot(hist.history['acc'])
plt.title('Model Training Accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.savefig('model-train-acc.png', bbox_inches='tight')
plt.clf()

plt.plot(hist.history['val_acc'])
plt.title('Model Testing Accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.savefig('model-test-acc.png', bbox_inches='tight')
plt.clf()

# summarize history for loss
plt.plot(hist.history['loss'])
plt.title('Model Training Loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.savefig('model-train-loss.png', bbox_inches='tight')
plt.clf()

plt.plot(hist.history['val_loss'])
plt.title('Model Testing Loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.savefig('model-test-loss.png', bbox_inches='tight')
