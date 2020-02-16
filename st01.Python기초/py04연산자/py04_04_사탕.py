#현재 5000원이 있고, 사탕의 가격은 120원, 최대한 살 수 있는 사탕의 개수와 나머지 돈 
myMoney = 5000
candyPrice = 120
# 최대한 살 수 있는 사탕 수
numcandies = myMoney // candyPrice
print(numcandies,"개")
# 최대한 사탕을 구입하고 남은 돈
change = myMoney%candyPrice
print(change,"원")
