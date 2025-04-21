# AudioKeyWordSearcher

Audio Keyword Search Tool
This script scans a directory (recursively) for audio files and finds those that contain a given keyword using OpenAI Whisper.

dependencies:
Whisper
FFMPEG (needs to be in PATH env variables)

Example Usage:
python find_sample_clips.py /path/to/audio/files

Matches will be printed to stdout with the file path and transcribed line.

Example from my usage (looking for the keyword "sample"):

PS C:\Users\Matth> python -u "h:\ANIMATION\Programs\Glitch\FindAudio.py" H:\ANIMATION\Assets\SFX\Helldiver_VO_Sharing_Folder
100%|███████████████████████████████████████| 139M/139M [00:03<00:00, 40.5MiB/s]
Scanning audio files:   5%|███████████████▍                                                                                                                                                                                                                                                                                                                             | 322/6938 [06:04<1:52:31,  1.02s/it]Found in H:\ANIMATION\Assets\SFX\Helldiver_VO_Sharing_Folder\Admiral_Lines_WAV\youre_simple_collect.wav:  Your sample collection is of great value to the Ministry of Science. Everything serves liberty in the end. Even our enemies.
Scanning audio files:   9%|███████████████████████████████▌                                                                                                                                                                                                                                                                                                             | 657/6938 [14:23<2:43:18,  1.56s/it]Found in H:\ANIMATION\Assets\SFX\Helldiver_VO_Sharing_Folder\All_Other_Files_In_US\1020612914.wav:  Keep an eye out for more samples next time.
Scanning audio files:  10%|███████████████████████████████▋                                                                                                                                                                                                                                                                                                             | 661/6938 [14:27<2:06:55,  1.21s/it]Found in H:\ANIMATION\Assets\SFX\Helldiver_VO_Sharing_Folder\All_Other_Files_In_US\1024460992.wav:  Well done! Lots of enemies killed, and lots of samples to help us figure out how to kill even more.
