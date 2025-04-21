import os
import whisper
from tqdm import tqdm
import argparse

# Allowed audio file extensions
AUDIO_EXTS = ['.wav', '.mp3', '.ogg', '.flac', '.m4a']
KEYWORD_MAIN = "sample"

def find_audio_files(root_dir):
    matches = []
    for root, _, files in os.walk(root_dir):
        for file in files:
            if any(file.lower().endswith(ext) for ext in AUDIO_EXTS):
                matches.append(os.path.join(root, file))
    return matches

def transcribe_and_filter(files, keyword=KEYWORD_MAIN):
    model = whisper.load_model("base")  # you can use "tiny" for speed or "small"/"medium" for accuracy, usually pretty fast as is
    results = []

    for audio_file in tqdm(files, desc="Scanning audio files"):
        try:
            result = model.transcribe(audio_file, fp16=False)
            if keyword.lower() in result["text"].lower():
                print(f"Found in {audio_file}: {result['text']}")
                results.append((audio_file, result["text"]))
        except Exception as e:
            print(f"Error with {audio_file}: {e}")
    
    return results

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Search audio files for keyword (e.g., 'word')")
    parser.add_argument("folder", help="Path to folder containing audio files")
    args = parser.parse_args()

    audio_files = find_audio_files(args.folder)
    matches = transcribe_and_filter(audio_files, keyword=KEYWORD_MAIN)

    if matches:
        print("\n--- Matches Found ---")
        for path, text in matches:
            print(f"{path}:\n  {text}")
    else:
        print("No matches found.")
