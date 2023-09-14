# path loop\\loopMission.py
# module loop.loopMission

#리스트 안의 튜플아이템 값들에 대해
#둘 중의 큰값과 작은값을 분류해서 출력 처리

# 방법 1 : 조건식 직접 작성
def practice1():
    nlist = [(12,45),(90,32),(56,19)]
    # for 문 안에서 if else 문 사용
    for (first,second) in nlist :
        if first > second :
            max = first
            min = second
        else :
            min = first
            max = second
        print(f'큰값 = {max}, 작은값 = {min}')

#방법 2 : 내장함수 이용
def practice2():
    nlist = [(12, 45), (90, 32), (56, 19)]
    #for문 안에서 내장함수 이용
    for(first, second) in nlist:
        tmax = max(first, second)
        tmin = min(first,second)
        print(f'큰값: {tmax}, 작은값: {tmin}')

#활용 실습 : 조건식 직접 작성하기
#리스트 안의 군집 아이템들이 가진 값들 중 각각 가장 큰 값을 골라 내서
#별도의 리스트에 저장 처리하고 출력
def practice3():
    lists = [[43,1,20] , (22,41,10,73), {12,32,45,3,9}]
    max_list = []

    #각 아이템별로 큰값을 골라내서 max_list에 저장 처리
    for item in lists:
        print(item, type(item))
        max_value = 0 #큰값 기록할 변수 준비
        for value in item:
            if max_value < value:
                max_value = value
        max_list.append(max_value)

    print(max_list)

#내장함수 max(Iterable) 사용
def practice4():
    lists = [[43,1,20] , (22,41,10,73), {12,32,45,3,9}]
    max_list = []

    #각 아이템별로 큰값을 골라내서 max_list에 저장 처리
    for item in lists:
        print(item, type(item))
        max_value = 0 #큰값 기록할 변수 준비
        for value in item:
            if max_value < value:
                max_value = value
        max_list.append(max_value)

    print(max_list)

'''
while 문 실습 문제
아래에 작성된 for문을 while문으로 변경하시오.

'''
#1. while 문으로 변경
def practice_while():
    sungjuk_list = [[12,'홍길동',98], [15,'김유신',87],[23,'황지니',45]]
    idx = 0
    while idx < len(sungjuk_list):
        student = sungjuk_list[idx]
        idx += 1
        if(student[2] >= 60):
            print('{}번 {}학생은 합격입니다.'.format(student[0], student[1]))
        else:
            print('{}번 {}학생은 불합격입니다.'.format(student[0], student[1]))
#2. for 문으로 변경
def practice_continue():
    sungjuk_list = [[12, '홍길동', 98], [15, '김유신', 87], [23, '황지니', 45]]

    for student in sungjuk_list:
        if(student[2] < 60):
            continue
        print('{}번 {}학생은 합격입니다.'.format(student[0],student[1]))

#print()안에 간단 if문 사용해서 출력 처리하기


def practice_short_if():
    sungjuk_list = [[12, '홍길동', 98], [15, '김유신', 87], [23, '황지니', 45]]

    for student in sungjuk_list:
        print(f'{student[0]}번 {student[1]}학생은 합격입니다.'if(student[2] >=60) else \
                  f'{student[0]}번 {student[1]}학생은 불합격입니다.')

#========================================================================================
import random
#랜덤 : 임의의 숫자(랜덤값)를 발생시키고자 할 때, random 모듈이 제공하는 함수를 사용할 수 있음

def test_random():
    print('임의의 랜덤값 :',random.random())
    #0.0 <= 랜덤값 < 1.0 범위의 임의의 실수형 값 발생함

    print('랜덤값 확인 :', random.randrange(1,11))
    #start <= 랜더값 < stop 범위의 임의의 정수형 값 발생함

#1부터 45까지의 임의의 정수 6개를 중복되지 않게 발생시켜서 저장하고
#오름차순정렬해서 출력 처리
def lotto():
    numbers = set() #numbers = {}
    #set 특징 : 중복허용 안 함, 저장 순서 없음
    while len(numbers) < 6:
        numbers.add(random.randrange(1,46))

    lotto_numbers = list(numbers) #set을 list로 바꿈
    lotto_numbers.sort(reverse=False) #오름차순정렬
    #sort()는 리스트 내부를 정렬함, 반환값 없음(None 리턴함)
    print('이번주 예상 로또 번호 :',lotto_numbers)




if __name__ == '__main__':
    # practice1()
    # practice2()
    # practice3()
    #test_random()
    lotto()