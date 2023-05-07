import numpy as np
import matplotlib.pyplot as plt
from keras import Sequential
from keras.layers import *
from keras import optimizers
from IPython.display import clear_output
from sklearn.model_selection import train_test_split
from src.preprocessing import preprocessing
from src.load_data import load_mfcc
from src.eval_functions import f1_m

def prepare_dataset(json_path, test_size=0.25, validation_size=0.2):    
    # Load data.json
    X, y = load_mfcc(json_path)

    # Train/test and validation split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = test_size)
    X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size = validation_size)
    X_train = X_train[..., np.newaxis]
    X_val = X_val[..., np.newaxis]
    X_test = X_test[..., np.newaxis]

    return X_train, X_val, X_test, y_train, y_val, y_test


def CNN(input_shape):
    # Define CNN model
    model = Sequential()
    model.add(Conv2D(64, (3, 3), activation = "relu", input_shape = input_shape))
    model.add(MaxPool2D((3, 3), strides=(2, 2), padding="same"))
    model.add(BatchNormalization())

    model.add(Conv2D(32, (3, 3), activation = "relu"))
    model.add(MaxPool2D((3, 3), strides=(2, 2), padding="same"))
    model.add(BatchNormalization())

    model.add(Conv2D(32, (2, 2), activation = "relu"))
    model.add(MaxPool2D((2, 2), strides=(2, 2), padding="same"))
    model.add(BatchNormalization())

    model.add(Conv2D(16, (1, 1), activation = "relu"))
    model.add(MaxPool2D((1, 1), strides=(2, 2), padding="same"))
    model.add(BatchNormalization())

    model.add(Flatten())
    model.add(Dense(64, activation="relu"))
    model.add(Dropout(0.3))
    model.add(Dense(10, activation="softmax"))

    return model
    
    
def plot_history(hist):
    plt.figure(figsize=(20,15))
    fig, axs = plt.subplots(2)
    # accuracy subplot
    axs[0].plot(hist.history["accuracy"], label="train accuracy")
    axs[0].plot(hist.history["val_accuracy"], label="val accuracy")    
    axs[0].set_ylabel("Accuracy")
    axs[0].legend(loc="lower right")
    axs[0].set_title("Accuracy eval")
    
    # Error subplot
    axs[1].plot(hist.history["loss"], label="train error")
    axs[1].plot(hist.history["val_loss"], label="val error")    
    axs[1].set_ylabel("Error")
    axs[1].set_xlabel("Epoch")
    axs[1].legend(loc="upper right")
    axs[1].set_title("Error eval")
    
    plt.show()


def model_eval(model, X_test, y_test):
    test_error, test_accuracy, test_f1 = model.evaluate(X_test, y_test, verbose=1)
    print(f"Test F1 score: {test_f1}")


def main_classification(json_path, show_history=False):
    # get dataset from prepare_dataset
    X_train, X_val, X_test, y_train, y_val, y_test = prepare_dataset(json_path)

    # define input shape
    input_shape = (X_train.shape[1],X_train.shape[2],X_train.shape[3])
    
    # create model
    model = CNN(input_shape)

    # compile model
    adam = optimizers.Adam(lr=1e-4)
    model.compile(optimizer=adam,
              loss="sparse_categorical_crossentropy",
              metrics=["accuracy", f1_m])

    hist = model.fit(X_train, y_train,
                 validation_data = (X_val, y_val),
                 epochs = 50,
                 batch_size = 32)
    
    # Show error/accuracy history
    if show_history:
        plot_history(hist)
    clear_output()

    # Model evaluation
    model_eval(model, X_test, y_test)

    return model