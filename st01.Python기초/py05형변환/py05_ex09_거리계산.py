# 지구에서 가장 가까운 별은 프록시마 켄타우리(Proxima Centauri) 별이라고 한다. 
# 프록시마 켄타우리는 지구로부터 40X 10**12 km 떨어져 있다고한다. 
# 빛의 속도(초속300000km)로 프록시마 켄타우리까지 간다면 시간이 얼마나 걸리는지 직접 계산해보기로 하자.

speed=300000 #초속 
distance=40*10**12 #거리=시간*속력
time_sec=distance/speed
time_min=time_sec/60
time_hour=time_min/60
time_day=time_hour/24
time_year=time_day//365
print(time_year,"년")
