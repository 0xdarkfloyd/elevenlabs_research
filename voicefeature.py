import librosa
import numpy as np
from scipy.signal import find_peaks
from scipy.stats import skew, kurtosis

def extract_features(file_path):
    # Load the audio file
    signal, sr = librosa.load(file_path)

    # Extract pitch features
    pitches, magnitudes = librosa.piptrack(y=signal, sr=sr)
    avg_pitch = np.mean(pitches)
    std_pitch = np.std(pitches)

    # Extract tone features
    tone = librosa.feature.tonnetz(y=signal, sr=sr)
    avg_tone = np.mean(tone)
    std_tone = np.std(tone)

    # Extract cadence features
    tempo, beats = librosa.beat.beat_track(y=signal, sr=sr)
    cadence = librosa.feature.tempo(y=signal, sr=sr)
    avg_cadence = np.mean(cadence)
    std_cadence = np.std(cadence)

    # Extract resonance features
    freqs = np.abs(librosa.stft(signal))
    avg_resonance = np.mean(freqs)
    std_resonance = np.std(freqs)

    # Extract articulation features
    articulation = librosa.feature.spectral_centroid(y=signal, sr=sr)
    avg_articulation = np.mean(articulation)
    std_articulation = np.std(articulation)

    # Extract accent features
    accent = librosa.feature.spectral_bandwidth(y=signal, sr=sr)
    avg_accent = np.mean(accent)
    std_accent = np.std(accent)

    # Extract speech pattern features

    rhythm = librosa.feature.rms(y=signal) #patched
    stress = librosa.feature.spectral_contrast(y=signal, sr=sr)
    intonation = librosa.feature.spectral_rolloff(y=signal, sr=sr)
    avg_rhythm = np.mean(rhythm)
    std_rhythm = np.std(rhythm)
    avg_stress = np.mean(stress)
    std_stress = np.std(stress)
    avg_intonation = np.mean(intonation)
    std_intonation = np.std(intonation)

    # Extract additional features
    skewness = skew(signal)
    kurtosis_value = kurtosis(signal)
    peak_count = len(find_peaks(signal)[0])

    # Return the extracted features
    return {
        'pitch': (avg_pitch, std_pitch),
        'tone': (avg_tone, std_tone),
        'cadence': (avg_cadence, std_cadence),
        'resonance': (avg_resonance, std_resonance),
        'articulation': (avg_articulation, std_articulation),
        'accent': (avg_accent, std_accent),
        'rhythm': (avg_rhythm, std_rhythm),
        'stress': (avg_stress, std_stress),
        'intonation': (avg_intonation, std_intonation),
        'skewness': skewness,
        'kurtosis': kurtosis_value,
        'peak_count': peak_count
    }

# Example usage
#file_path = 'example_mimosa.mp3
file_path = 'example_jacky.mp3'
features = extract_features(file_path)
for feature, values in features.items():
    print(f'{feature}: {values}')