import tkinter as tk
import os
from pydub import AudioSegment
from tkinter import filedialog

root = tk.Tk()
root.withdraw()  # 메인 윈도우 숨기기

file_path = filedialog.askopenfilename()  # 파일 선택창 열기
# 파일 경로에서 폴더 경로 추출
folder_path = os.path.dirname(file_path)

print("선택한 파일:", file_path)

input_path = file_path
output_path = os.path.splitext(file_path)[0] + ".mp3"  # 확장자를 .md로 변경
print("내보낼 파일:", output_path)
audio_ext = os.path.splitext(file_path)[1] # 확장자 추출
# FLAC 파일 불러오기
audio = AudioSegment.from_file(input_path, format="flac")

# MP3 파일로 변환하여 저장
audio.export(output_path, format="mp3")
