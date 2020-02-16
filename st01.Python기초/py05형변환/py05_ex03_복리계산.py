#1626년에 아메리카 인디언들이 뉴욕의 맨하탄섬을 단돈 60길더(약 24달러)에 탐험가 Peter Minuit에게 팔았다고 한다. 
# 382년 정도 경과한 현재 맨하탄 땅값은 약 600억달러라고 한다.
#하지만 만약 인디언이 24달러를 은행의 정기예금에 입금해두었다면 어떻게 되었을까? 
# 예금 금리는 복리로 6%라고 가정하자. 그리고 382년이 지난후에는 원리금을 계산하여 보자.

initial_money=24
interest=0.06
years=382
total=initial_money*(1+interest)**years
banktotal=round(total)
print(banktotal)
manhattan=600000000000

if banktotal>manhattan :
    print("예금")
else:
    print("부동산")