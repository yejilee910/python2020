
# step1. ArrayList 인스턴스, list  만들기.
# step2. 심사 위원수를 입력 받는다.
# step3. 심사 위원의 점수 입력 받아서 list에 저장.
#     몇 번 입력 받아야 하는가? 심사 위원수 만큼
# step4. 합계를 구하는 메서드 만들기
#     1번방부터 마지막방 -1 까지
# step5. 평균을 구하는 메서드 만들기.
#     평균값 = (double)sum / ( list.size() - 2 )
# step6. ArrayLis 정렬하기.
# step7. 합계를 구하고 출력한다.
# step8. 평균을 구하고 출력한다.

jugde = int(input("심사 위원의 수를 입력하시오: "))
i = 0
grade_list = []
for i in range(0, jugde, 1):
    grade = int(input("심사 위원의 점수 입력 : "))
    grade_list.append(grade)
    i += 1

grade_list.sort()

del grade_list[grade_list.index(max(grade_list))]
del grade_list[grade_list.index(min(grade_list))]
grade_list.sort()
print("유효점수:", grade_list)
total = sum(grade_list)
count = len(grade_list)
average = total/count
print('합계:', total)
print('평균:' '%0.2f' % average)
