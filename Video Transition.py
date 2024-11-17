import os.path
import ffmpeg
from tkinter import filedialog

file_path = filedialog.askopenfilename()
print("선택한 파일 : ", file_path)
folder_path = os.path.dirname(file_path)

output_file = os.path.splitext(file_path)[0] + ".mp4"  # 확장자를 .mp4로 변경
i = 0
while os.path.exists(os.path.join(folder_path, output_file)):
    i = i + 1
    output_file = os.path.splitext(file_path)[0] + "_" + str(i) + ".mp4"
print("내보낼 파일 :", output_file)

#ffmpeg.input(file_path).output(output_file, vcodec='libx264', acodec='aac', video_bitrate = '500k', s='1280x720',r=24).run()
ffmpeg.input(file_path).output(output_file, vcodec='copy', acodec='copy', video_bitrate = '500k', s='1280x720',r=24).run()
#subtitle_file = os.path.splitext(file_path)[0] + ".smi"
#print("자막 파일 :", subtitle_file)
#(
#    ffmpeg
# .input(file_path)
# .filter("subtitles", subtitle_file)
# .output(output_file, vcodec='copy', acodec='copy', video_bitrate = '500k', s='1280x720',r=24)
# .run()
# )

#ffmpeg.input(file_path).output(output_file, vcodec='h264', acodec='aac', video_bitrate = '500k', s='1280x720',r=24,vf=f'subtitles={subtitle_file}').run()
#ffmpeg.input(file_path).output(output_file, vcodec='h264', acodec='aac', video_bitrate = '500k', s='1280x720',r=24).run()
    #vf=f'subtitles={subtitle_file}'

