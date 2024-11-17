import re
import os
import chardet
from tkinter import filedialog

# SMI 파일 경로 설정
smi_file_path = filedialog.askopenfilename()

#SMI 파일 인코딩 감지
with open(smi_file_path, 'rb') as file:
    raw_data = file.read()
    result = chardet.detect(raw_data)
    file_encoding = result['encoding']
    print(file_encoding)

# SRT 파일 내용 저장 리스트
srt_subtitle = []
#srt_subtitle = ""

# SMI 파일 읽기
with open(smi_file_path, 'r', encoding=file_encoding) as file:
    lines = file.readlines()
    #smi_content = file.read()
i = 0
for line in lines:
    if "<SYNC" in line:
        start_time = int(re.search(r'Start=(\d+)', line).group(1))
        start_time = f"{start_time:09}" #9자리 숫자로 포멧 변경
        start_h = f"{start_time[:2]}"
        start_m = f"{start_time[2:4]}"
        start_s = f"{start_time[4:6]}"
        start_ms = f"{start_time[6:9]}"
        if "<SYNC" in lines[i+2]:
            end_time = int(re.search(r'Start=(\d+)', lines[i+2]).group(1))
    elif "<P Class=" in line:
        #if "</BODY>" in lines[i+1]:
        #    end_time = int(re.search(r'Start=(\d+)', lines[i + 2]).group(1)) + 2000
        end_time = f"{end_time:09}"  # 9자리 숫자로 포멧 변경
        end_h = f"{end_time[:2]}"
        end_m = f"{end_time[2:4]}"
        end_s = f"{end_time[4:6]}"
        end_ms = f"{end_time[6:9]}"
        text = re.sub(r'<.*?>', '', line).strip()  # 태그 제거
        # SRT파일 저장
        srt_subtitle.append(f"{int((i - 16)/2)}\n{start_h:02}:{start_m:02}:{start_s:02},{start_ms:03} --> {end_h:02}:{end_m:02}:{end_s:02},{end_ms:03}\n{text}\n")
    i = i + 1
srt_file_path = os.path.splitext(smi_file_path)[0] + '.srt'
with open(srt_file_path, 'w', encoding='utf-8') as file:
    file.write('\n'.join(srt_subtitle))
print(f'SRT 파일 생성 완료: {srt_file_path}')