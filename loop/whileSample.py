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

if __name__ == '__main__':
    test_while()