import librosa
import matplotlib.pyplot as plt
import numpy as np

def visualise(dataset_path, json_path, songpath): 
    for i in range(2):
        audio, sfreq = librosa.load(songpath+str(i)+".wav")
        time = np.arange(0, len(audio))/sfreq
        plt.plot(time,audio)
        plt.xlabel("Time")
        plt.ylabel("Sound Amplitude")
        plt.show()

        
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