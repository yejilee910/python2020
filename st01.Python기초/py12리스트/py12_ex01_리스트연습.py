
pos = 0
value = ""

#  List 선언
Flist = []


#  C: 추가. 검색: "파이썬 리스트 추가"
#  MILK, BREAD, BUTTER 순으로 추가
#
Flist.append("MILK")
Flist.append("BREAD")
Flist.append('BUTTER')

#  APPLE 삽입. 검색: "파이썬 리스트 삽입"
#  특정 위치에 추가하기
#  "BREAD" 앞에 "APPLE" 삽입
Flist.insert(1, "APPLE")
print(Flist)
#  "BREAD" 가 들어있는 방번호 찾기
print(Flist.index("BREAD"))

#  R: 읽기
#  BUTTER 값을 출력하시오.
#  "BUTTER" 가 들어있는 방번호 찾기
print(Flist[Flist.index("BUTTER")])

#  U: 수정. 검색: "파이썬 리스트 수정"
#  "BREAD" 를 "GRAPE"로 변경
#  "BREAD" 가 들어있는 방번호 찾기

Flist[Flist.index("BREAD")] = "GRAPE"
print(Flist)

#  D: 인덱스로 삭제. 검색: "파이썬 리스트 삭제"
#  인덱스를 이용하여 GRAPE 를 삭제

del Flist[Flist.index("GRAPE")]
print(Flist)

#  D: 값으로 찾아서 삭제. 검색: "파이썬 리스트 값으로 삭제"
#  값으로 MILK를 찾아서 삭제하시오

Flist.remove("MILK")
print(Flist)


#  P: 리스트를 for문으로 출력.
#  검색: "파이썬 리스트 for 출력"
#  검색: "파이썬 리스트 크기"
#
for i in Flist:
    print(i)

for i in range(0, len(Flist), 1):
    print(i, Flist[i])


#  P: 리스트를 for-each문으로 출력.
#


#  테스트용 데이터 생성을 위한 코드. 수정하지 마시오.
for i in range(4):
    Flist.append("APPLE")
    Flist.append("BANANA")
print(Flist)

#  S: 검색: "파이썬 리스트 검색
#  첫번째 APPLE을 찾으시오.
Flist.index("APPLE", 0, 1)


#  S: 오름차순 정렬. 검색: "파이썬 리스트 오름차순 정렬"

Flist.sort(reverse=False)
print(Flist)

#  S: 내림차순 정렬. 검색: "파이썬 리스트 내림차순 정렬"
Flist.sort(reverse=True)
print(Flist)
#  검색2. APPLE 이 몇개 있나요?
print(Flist.count("APPLE"))

#  변환된 배열을 for 문으로 출력.
for i in range(0, len(Flist), 1):
    print(i, Flist[i])

print("list의 모든 값을 while문을 사용하여 삭제하시오")
print(len(Flist))
i = 0
while i < len(Flist):
    del Flist[i]

print(Flist)
