#test_bool\\operator_sample.py or test_bool/operator_sample.py
#모듈로 표현 : test_bool.operator_sample

#bool 자료형 확인
def func_bool():
    flag = True
    print('flag :',flag,type(flag))

    flag = False
    print('flag :', flag, type(flag))

    #파이썬에서는 대소문자 구분함
    #flag = true #NameError

#bool() 함수 사용 : 값의 논리상태를 확인할 때 사용함
def func_bool2():
    print('결과1 :',bool('abcd')) #True
    print('결과2 :',bool('')) #False
    
    #값이 저장되어 있는지, 비어 있는지 확인하는 용도로 사용할 수 있음
    print(bool({'a':1, 'b':2})) #True
    print(bool({})) #False
    
    print(bool([1,2,3,4]))  #True
    print(bool([])) #False
    
    print(bool((1,2,3))) #True
    print(bool(())) #False
    
    print(bool(23)) #True
    print(bool(0)) #False
    
#비교(관계) 연산자
#2개의 값을 가지고 크냐(>, 초과), 작으냐(<, 미만),
#같으냐(==), 같지 않느냐(!=), 크거나 같으냐(>=, 이상), 작거나 같으냐(<=, 이하)
#이항 연산자 : 값1 연산자 값2
def func_compare():
    print('1==1 :', 1==1) #True
    print('1==2 :', 1==2) #False

    print('1 > 0 :', 1 > 0)  # True
    print('1 < 2 :', 1 < 2)  # True

    print('1>=1 :', 1 >= 1)  # True
    print('1!=0 :', 1 != 0)  # True
    
#논리 연산자 : 논리값(True, False)을 계산에 사용하는 연산자
#and, or, not 
def func_logic():
    a = 1
    b = 2
    
    print(a >0 and b > 1) #True and True ---> True
    print(a == 0 or b != 1)  # False or True ---> True
    
    #and 연산자의 특징 : 
    #앞 and 뒤 : 앞이 False이면 뒤를 실행 안 함
    #앞이 True이면 뒤를 실행함
    print('a' and 'b') #앞이 True이므로 뒤를 실행, 'b'가 출력됨
    print('' and 'b') #앞이 False이므로 뒤를 실행 안 함, ''가 출력됨
    
    #or 연산자의 특징 :
    #앞 or 뒤 : 앞이 True이면 뒤를 실행 안 함, 앞이 False이면 뒤를 실행함
    print('a' or 'b') #앞이 True이므로 뒤 실행 안 함, 'a'가 출력됨