# path : loop\\whileSample.py
# module : loop.whileSample
#while 문 사용 테스트 스크립트
'''
while(반복에 대한 조건식) :
    반복 실행 구문
'''
def test_while():
    num = 5
    while num > 0:
        print(num)
        num-=1

#반복에 대한 조건식 대신에 True를 사용할 수도 있음
#주의 : 무한루프가 되지 않게 if조건문과 break문을 반복문 안에 작성함
def test_while2():
    num = 5
    while True:
        print(num)
        num -=1
        if num == 0:
            break

#반복 횟수가 정해지지 않은 경우 while 문을 주로 사용함
#문자 하나를 입력받아서, 그 문자의 유니코드를 출력하는 처리를 반복
#단, 0이 입력되면 반복이 종료됨
def print_unicode():
    ch = input('문자 하나를 입력 [0 입력시 종료됨] :')

    while ch != '0':
        print(f'{ch} is unicode {ord(ch)}')
        ch = input('문자 하나를 입력 [0 입력시 종료됨] :')

def print_unicode2():
    while True:
        ch = input('문자 하나를 입력 [0 입력시 종료됨] :')
        if ch =='0':
            break
        print(f'{ch} is unicode {ord(ch)}')

#파이썬에서는 여러 줄의 문자열을 표현할 때 3쌍의 따옴표를 이용할 수 있음
def display_menu():
    prompt='''
    ※ 원하는 메뉴 번호를 선택하세요. ※
    
    1. 추가
    2. 삭제
    3. 출력
    4. 끝내기
    '''
    #print(prompt)
    while True:
        print(prompt)
        no = int(input('번호 입력 : '))

        if no == 4:
            break
    print('======= end =======')

#함수 실행
if __name__ == '__main__':
    #test_while()
    #test_while2()
    #print_unicode()
    #print_unicode2()
    display_menu()