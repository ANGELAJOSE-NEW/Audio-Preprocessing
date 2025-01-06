import librosa
import soundfile as sf
import os

def normalize_audio(input_path, output_path):
    try:
        # Load the audio file
        audio, sr = librosa.load(input_path, sr=None)
        
        # Normalize the audio to a range of -1 to 1
        max_amplitude = max(abs(audio))
        if max_amplitude > 0:
            audio = audio / max_amplitude

        # Ensure the output directory exists
        output_dir = os.path.dirname(output_path)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Save the normalized audio
        sf.write(output_path, audio, sr)
        print(f"Normalized: {input_path} -> {output_path}")
    except Exception as e:
        print(f"Error processing {input_path}: {e}")

if __name__ == "__main__":
    input_dir = "C:/Users/sonyj/OneDrive/Desktop/Audio Preprocessing/Processed audio/"
    output_dir = "C:/Users/sonyj/OneDrive/Desktop/Audio Preprocessing/Processed audio/"

    for file_name in os.listdir(input_dir):
        if file_name.endswith(".wav"):
            input_path = os.path.join(input_dir, file_name)
            output_path = os.path.join(output_dir, file_name)  # Save to output directory
            normalize_audio(input_path, output_path)  # Do not overwrite the input file
