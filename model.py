import os
import librosa
import librosa.display
import matplotlib.pyplot as plt

def tempo(audio):
    y, sr = librosa.load(audio)
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    return str(tempo)

def waveshow(audio):
    y, sr = librosa.load(audio)
    plt.figure(figsize=(14, 5))
    librosa.display.waveplot(y, sr=sr)
    filename_str = os.path.basename(audio)
    filename_str = filename_str.replace("wav", "jpg")
    plot_file_path = "static/images/" + filename_str
    print(plot_file_path)
    plt.savefig(plot_file_path)
    return plot_file_path



