# 텍스트 파일을 읽어서 단어를 얼마나 다양하게 사용하여 문서를 작성하였는지를 계산하는 프로그램을 작성해보자.

#단어에서 구두점을 제거하고 소문자로 만든다. 
def process(w) :
    output = ""
    for ch in w : 
        if ( ch.isalpha() ) : 
            output += ch 
    return output.lower()
words = set()

#파일 열기
fname = input("파일이름 입력 : ")
file = open(fname, "r")

#파일의 모든 줄에 대하여 반복한다. 
for line in file : 
    lineWords = line.split()
    for word in lineWords : 
        words.add(process(word))   #단어를 세트에 추가 

print("사용된 단어의 개수 = ", len(words))
print(words)
