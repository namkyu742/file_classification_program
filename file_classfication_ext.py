import os
import shutil
import glob

PATH_INPUT = 'E:\\NNNN-1\\'
PATH_OUTPUT = 'E:\\NNNN\\'

file_list = os.listdir(PATH_INPUT)

for file in file_list:
    temp = file
    temp = temp.replace("[", "[[]")             # glob에서 '['를 메타문자로 인식하기 때문에 대괄호로 한번 감싸준다.
    files = glob.glob(PATH_INPUT+temp+"\\*.webp")

    for name in files:
        if not os.path.isdir(name):             # 디렉토리는 포함 x
            src = os.path.splitext(name)        # 확장자와 파일명 구분
            os.rename(name,src[0]+'.png')       # webp를 없앤 파일명에 png확장자 붙이기
    
 

    temp = file.split("] ")
    folder_name = temp[0]
    folder_name = folder_name.replace("[", "")
    folder_name = folder_name.replace(" ", "_")
    folder_name = folder_name.lower()

    if not os.path.exists(PATH_OUTPUT+folder_name):
        os.makedirs(PATH_OUTPUT+folder_name)
        
    shutil.move(PATH_INPUT+file ,PATH_OUTPUT+folder_name)      # 파일 옮기기


print("done!")

# -- 개발 최종본-- 
# [동작 순서]
# 지정한 폴더 내부의 목록을 가져온다.
# 2. 폴더 이름을 하나씩 읽는다.
# 3. 해당 폴더에서 특정 조건을 만족하게 다른 위치에 새로운 폴더를 생성한다.
# 4. 단, 해당 폴더가 이미 존재한다면 생성은 건너뛴다.
# 5. 또한, 본 프로그램에서의 특정조건이란 다음과 같다.
#    폴더 이름에서 '['와 ']' 사이의 문자를 가져오되 공백은 '_'로 치환하고 대문자는 전부 소문자로 치환한다.
# 6. 생성한 폴더로 폴더를 옮긴다.

# pyinstaller -w -F file_classfication_ext.py


# 2022-06-06 기능 추가
# txt형식의 옵션파일을 설정하여 본래의 고정된 기능에서 확장한다.
# ㄴㄴ 안할래