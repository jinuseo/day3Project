# loop\\forMission1.py
# module : loop.forMission1

'''
키보드로 문자열을 입력받아서, 요구대로 처리하고 출력하시오.
실행 :
    문자열 입력 : apple (value : str)
처리내용 :
 for문 사용 : 글자의 유니코드 출력이 반복되게 함

 소문자는 모두 대문자로 변환해서 출력 처리함 : 반복 종료 후 출력 처리함
 APPLE
'''
def practice():
    value = input('문자열을 입력 : ')

    for i in value:
        print(ord(i))
    print(value.upper())