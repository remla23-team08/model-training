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