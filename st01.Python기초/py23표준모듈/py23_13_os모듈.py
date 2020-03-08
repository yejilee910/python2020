
# 모듈을 읽어 들입니다.
import os

# os.path.isfile() # 파일의 존재 유무를 확인하는 method

# 1. 상대 경로를 사용하는 경우
#    ../parentfolder
#     ./currentfolder

# 2. 절대 경로를 사용하는 경우
# 윈도우 - C:\\Desktop\aa.txt
# 맥 /Users/yejilee/folder

# 현재 폴더에 phone.txt 파일의 존재유무확인
print(os.getcwd())
if os.path.isfile("./py23표준모듈/phone.txt"):
    print("파일이 존재")
else:
    print("파일 없음")

print(os.listdir("."))
# 기본 정보를 몇 개 출력해봅시다.

# 폴더를 만들고 제거합니다[폴더가 비어있을 때만 제거 가능].

# 파일을 생성하고 + 파일 이름을 변경합니다.

# 파일을 제거합니다.


# 파일 존재 유무 체크

# 현재 폴더의 파일/폴더를 출력합니다.

# 현재 폴더의 파일/폴더를 구분합니다.

# 폴더를 읽어 들이는 함수
