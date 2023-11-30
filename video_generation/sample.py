from mutagen.mp3 import MP3
from PIL import Image
from pathlib import Path
import os
import imageio
from mutagen.mp3 import MP3
from moviepy.editor import ImageSequenceClip, AudioFileClip, CompositeAudioClip
from moviepy import editor
audio_path = os.path.join(os.getcwd(), "story.mp3")
bgm_path = os.path.join(os.getcwd(), "bgm.mp3")
video_path = os.path.join(os.getcwd(), "videos")
images_path = os.path.join(os.getcwd(), "images")
audio = MP3(audio_path)
bgm_volume = 0.05
bgm_audio = AudioFileClip(bgm_path).volumex(bgm_volume)
audio_length = audio.info.length


list_of_images = []
for image_file in os.listdir(images_path):
    if image_file.endswith('.png') or image_file.endswith('.jpg'):
        image_path = os.path.join(images_path, image_file)
        image = Image.open(image_path).resize((400, 400), Image.ANTIALIAS)
        list_of_images.append(image)

duration = audio_length/len(list_of_images)
imageio.mimsave('images.gif', list_of_images, fps=1/duration)

video = editor.VideoFileClip("images.gif")
audio = editor.AudioFileClip(audio_path)
# f_video = video.set_audio(audio)

# Combine the audio clips
final_audio = CompositeAudioClip([audio, bgm_audio.set_duration(audio.duration)])

# Set the combined audio to the video
final_video = video.set_audio(final_audio)

os.chdir(video_path)
final_video.write_videofile(fps=60, codec="libx264", filename="video1.mp4")
