#파이썬 제어문 실습용 시작 스크립트

#import test_bool.operator_sample
#다른 파일에 있는 함수를 사용하려면 import 선언해야함
#import 디렉토리명.파일명
#모듈명이 길거나 복잡할 경우 줄임말 지정 가능함
#import 모듈명 as 줄임말

#import conditional.ifSample as cif

import test_bool.operator_sample as to

import conditional.ifMission1 as cm1
import conditional.ifelseMission2 as cm2
import conditional.ifelseMission3 as cm3

import loop.forSample as lf

import loop.forMission1 as m1

#프로그램을 시작하는 구문임
if __name__ == '__main__':
    #import한 파일에서 제공하는 함수 사용
    #모듈명.함수명()
    #test_bool.operator_sample.func_bool()

    #연산자 사용 테스트
    #to.func_bool()
    #to.func_bool2()
    #to.func_compare()
    #to.func_logic()

    #조건문 사용 테스트
    #cif.test_if()
    #cif.test_if2()
    #cif.test_even()
    #cif.test_even2()
    #cif.test_range()
    #cif.test_in()
    #cif.checkPayment()
    #cif.checkPayment2()
    #cif.multi_if()
    #cif.shortCondition()
    #cif.shortCondition2()

    #조건문 실습문제
    # cm1.practice1()
    # cm2.practice2()
    # cm3.practice3()

    #for문 사용 테스트
    #lf.test_for1()
    #lf.for_sum()
    #lf.test_iterable()
    #lf.test_range()
    #lf.for_indexing()
    #lf.print_gugudan()
    #lf.doubleFor()
    #lf.list_in_list()
    #lf.list_in_list2()
    lf.list_in_list3()

    #반복문 실습문제
    #m1.practice()