# path : loop\\loopSample.py
# module : loop.loopSample

#필요한 경우 반복문 안에 조건문을 사용할 수도 있음
#문자열에서 특정 문자가 포함된 갯수를 조회한다면
#문자열과 찾을 문자를 입력받고, 문자열 안의 찾는 문자의 갯수 조회하기
def loop_in_conditional():
    st = input('문자열 입력 : ')
    ch = input('찾는 문자 입력 :')
    cnt = 0

    for c in st:
        if c == ch:
            cnt += 1

    print(f'{st}안에 포함된 {ch} 문자의 갯수는 {cnt} 개임')

#문자열 안의 찾는 문자를 제외한 글자 갯수 조회하기
def loop_in_conditional2():
    st = input('문자열 입력 : ')
    ch = input('찾는 문자 입력 :')
    cnt = 0

    for c in st:
        if c != ch:
            cnt += 1

    print(f'{st}안에 포함된 {ch} 문자를 제외한 문자의 갯수는 {cnt} 개임')

'''
분기문 : continue, break (반복문 안에서만 사용할 수 있는 문장임)
    반복 실행의 흐름을 바꾸는 문장
    for or while 반복조건 :
        if 조건식:
            continue or break
            continue: 반복을 중간 생략함(아래의 내용을 실행하지 않고 다음 반복으로 넘어감)
            break: 반복을 종료함
    
'''
#1부터 100까지 정수중에서 짝수들의 합계만 구하는 경우
#range(), continue를 이용함
def sum_even_1to100():
    sum = 0
    for n in range(1,101):
        if n % 2 ==1:
            continue
        print(n,'+',end='')
        sum += n
    print(f'\n1부터 100까지 짝수들의 함계 : {sum}')

#리스트 안에 튜플이 여러 개 저장된 경우
#튜플을 꺼내서 각 값을 변수에 저장할 경우, (변수명, 변수명, ...) 소괄호로 묶어서 변수 저장함
def list_in_tuple():
    nlist = [(12, 45), (90, 32), (56,19)]

    for item in nlist:
        print(item)

    for a, b in nlist:
        print(a,b)

    for(a,b) in nlist:
        print(a,b)

#함수 실행
if __name__ == '__main__':
    #loop_in_conditional()
   #loop_in_conditional2()
   #sum_even_1to100()
   list_in_tuple()