# 자동 판매기를 시뮬레이션하는 프로그램을 작성하여 보자. 
# 사용자는 1000원짜리 지폐와 500원짜리 동전, 100원짜리 동전을 사용할 수 있다. 
# 물건값을 입력하고 1000원권, 500원짜리 동전, 100원짜리 동전의 개수를 입력하면 
# 거스름돈을 계산하여서 동전으로 반환한다. 

product=float(input("물건 값을 입력하세요 : "))
thousand=int(input("1000원 지폐개수 : "))
five=int(input("500원 동전개수: "))
ten=int(input("100원 동전개수: "))

totalvalue=thousand*1000+five*500+ten*10
change=totalvalue-product 

#거스름돈(1000원 개수)를 계산
change_thousand=change//1000
# 거스름돈(500원 동전 개수)을 계산한다. 
change=change-change_thousand*1000
change_five=change//500
# 거스름돈(100원 동전 개수)을 계산한다. 
change=change-change_five*500
change_hun=change//100
# 거스름돈(10원 동전 개수)을 계산한다. 
change=change-change_hun*100
change_ten=change//10
# 거스름돈(1원 동전 개수)을 계산한다. 
change=change-change_ten*10
change_one=change//1
# 출력
print("1000원=",change_thousand,"개","500원=",change_five,"개", "100원=",change_hun,"개","10원=",change_ten,"개","1원=",change_one,"개")