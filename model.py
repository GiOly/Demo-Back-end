import os
import librosa
import librosa.display
import matplotlib.pyplot as plt

def mfcc(audio):
    y, sr = librosa.load(audio)
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40)
    return str(mfccs)

def waveshow(audio):
    y, sr = librosa.load(audio)
    plt.figure(figsize=(14, 5))
    librosa.display.waveplot(y, sr=sr)
    filename_str = str(audio.filename)
    plot_file_path = "static/images/test.jpg"
    plt.savefig(plot_file_path)



