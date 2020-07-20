import librosa

def mfcc(filename):
    y, sr = librosa.load(filename)
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40)
    return mfccs
