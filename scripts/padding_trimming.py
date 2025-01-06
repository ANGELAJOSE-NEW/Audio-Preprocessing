import librosa
import numpy as np
import soundfile as sf
import os

def trim_silence(input_path, output_path, top_db=20):
    try:
        # Load the audio file
        audio, sr = librosa.load(input_path, sr=None)
        
        # Detect and split non-silent regions
        non_silent_intervals = librosa.effects.split(audio, top_db=top_db)
        
        # Concatenate all non-silent regions
        trimmed_audio = np.concatenate([audio[start:end] for start, end in non_silent_intervals])
        
        # Save the trimmed audio
        sf.write(output_path, trimmed_audio, sr)
        print(f"Trimmed silence: {input_path} -> {output_path}")
    except Exception as e:
        print(f"Error processing {input_path}: {e}")

if __name__ == "__main__":
    input_dir = "C:/Users/sonyj/OneDrive/Desktop/Audio Preprocessing/Processed audio/"
    output_dir = "C:/Users/sonyj/OneDrive/Desktop/Audio Preprocessing/Processed audio/"

    # Ensure output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for file_name in os.listdir(input_dir):
        if file_name.endswith(".wav"):
            input_path = os.path.join(input_dir, file_name)
            output_path = os.path.join(output_dir, file_name)
            trim_silence(input_path, output_path)
