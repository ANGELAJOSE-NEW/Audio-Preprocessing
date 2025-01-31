import librosa
import os
import soundfile as sf

def resample_audio(input_path, output_path, target_sr=16000):
    audio, sr = librosa.load(input_path, sr=None)
 
    resampled_audio = librosa.resample(audio, orig_sr=sr, target_sr=target_sr)
    # librosa.output.write_wav(output_path, resampled_audio, sr=target_sr)
    sf.write(output_path, resampled_audio, target_sr)

if __name__ == "__main__":
    input_dir = "C:/Users/sonyj/OneDrive/Desktop/Audio Preprocessing/Audio files/"
    output_dir = "C:/Users/sonyj/OneDrive/Desktop/Audio Preprocessing/Processed audio/"

    for file_name in os.listdir(input_dir):
        if file_name.endswith(".wav"):
            input_path = os.path.join(input_dir, file_name)
            output_path = os.path.join(output_dir, file_name)
            resample_audio(input_path, output_path)
