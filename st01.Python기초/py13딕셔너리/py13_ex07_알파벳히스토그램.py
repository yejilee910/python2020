# 영문자로 구성된 텍스트를 입력받아 영문자 알파벳의 히스토그램을 만들어보자. 이 도전 문제는 문자열과 딕셔너리를 다루는 연습을 위한 것이다. 단, 대문자와 소문자는 같은 것으로 다룬다.

# 작업순서
# 1. 파일을 읽고 문자열에 텍스트를 저장
# 2. 기존 str의 줄바꿈(\n)을 제거하여 한 줄의 string 으로 만든다. str = str.replace("\n", " ")
# 3. Dictionary table 을 만든다
# 4. 문자열을 split()해서 array 리스트로 만든다.
# 5. 반복문을 사용하여 array 리스트를 루프돌면서,
# 1) 리스트요소에서 첫글자를 추츨한다. 선택연산자[] 사용
#     val = array[i][0] 또는 val = i[0]
# 2) 딕셔너리 table 에서 키값중에 val이 있는지 찾는다.
# 3) 찾았다면 table[val] = table[val] + "-"
#     아니면 table[val] = "-"
# 6. 찾기가 끝나면 table 출력한다.

str = """This was a great help. 
I applied this method to similiar problem 
and rather than concat a SELECT statement 
I created an event scheduled every couple 
hours to rebuild a view that pivots n amount 
of rows from one table into n columns on the other. 
It is a big help because before I was rebuilding 
the query using PHP on every execution of the SELECT. 
Even though views can not leverage Indexes, 
I am thinking filtering performance will not 
be an issue as the pivoted rows->columns 
represent types of training employees at a 
franchise have so the view will not ever break 
a few thousand rows."""

str = str.replace("\n", "")
array = str.split()

table = dict()
for i in array:
    val = i[0]
    val = val.upper()  # 대소문자 구분을 없애기 위해 모두 대문자로 치환
    if val in table:
        table[val] = table[val] + "-"
    else:
        table[val] = "-"

print("히스토그램을 그립니다")
for key, value in sorted(table.items()):
    print(key,value)

