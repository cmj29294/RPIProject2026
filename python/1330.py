#첫째 줄에 다음 세 가지 중 하나를 출력한다.

#A가 B보다 큰 경우에는 '>'를 출력한다.
#A가 B보다 작은 경우에는 '<'를 출력한다.
#A와 B가 같은 경우에는 '=='를 출력한다.

#A= input('숫자를 입력해주세요. ')
#B= input('숫자를 입력해주세요. ')
#print(type(A))
#print(A,B)
#print(A+B)

A, B= input().split()
A, B= int(A), int(B)

if A > B :
    print('>')
elif A < B :
    print('<')
else :
    print('==')