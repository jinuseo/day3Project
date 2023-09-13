# path : loop\\whileMission.py
# module : loop.whileMission
#while문 실습문제
'''
prompt 변수를 while문으로 반복해서 출력하면서, 입력되는 번호에 따라 sungjuk_list의 아이템을 추가하거나
삭제하거나 출력되게 작성하시오.
1. 입력 : 리스트에 아이템 값들을 입력받아 추가함
    번호 : 24 (sno : int)
    이름 : 이순신 (sname : str)
    점수 : 100 (score : int)
==> 리스트에 추가 처리함 ==> '새로운 학생정보가 추가되었습니다.' 출력함
2. 입력 : 리스트의 인덱스 위치의 아이템을 제거함
'현재 저장된 아이템의 갯수는 3개입니다.' 출력함
제거할 아이템의 순번 : 3 ==> 입력받은 인덱스 위치의 아이템을 제거함
==> '3번 위치의 아이템이 제거되었습니다' 출력함 ==> '현재 저장된 아이템의 갯수는 2개입니다.' 출력함
==> 잘못된 인덱스 입력시 : '순번이 잘못 입력되었습니다. 확인하고 다시 입력하세요.' 출력함
3. 입력 : 저장된 리스트 정보를 아이템 별로 출력함
 0 : [12, '홍길동', 98]
 1 : [15, '김유신', 87]
 2 : ......
4. 입력 : while 반복 종료함
    '성적 관리 프로그램이 종료되었습니다.' 출력함
'''

def sungjuk_process():
    sungjuk_list = []
    prompt = '''
    ※ 원하는 메뉴 번호를 선택하세요. ※

    1. 추가
    2. 삭제
    3. 출력
    4. 끝내기
    '''
    # print(prompt)
    while True:
        print(prompt)
        no = int(input('번호 입력 : '))

        if no == 1:
            sungjuk_list.append([int(input('번호 :')),input('이름 :'), int(input('점수 : '))])
            print('새로운 학생정보가 추가되었습니다.')

        if no == 2:
            print(f'현재 저장된 아이템의 갯수는 {len(sungjuk_list)}개 입니다.')
            index = int(input('삭제할 인덱스의 위치 입력 : '))
            sungjuk_list.pop(index)
            print(f'{index}번 위치의 아이템이 제거되었습니다.')
            print(f'현재 저장된 아이템의 갯수는 {len(sungjuk_list)}개 입니다.')
        # else:
        # print('순번이 잘못 입력되었습니다. 확인하고 다시 입력하세요.')

        if no == 3:
            for i in sungjuk_list:
                print(i)

        if no == 4:
            break
    print('======= end =======')

if __name__ == '__main__':
    sungjuk_process()