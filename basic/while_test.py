listdata=[]

while True:
    print('''
    =====리스트 데이터 관리=====
    1.추가 2.수정 3.삭제 4.종료
    ===========================
    ''')

    menu=int(input('메뉴를 선택하시오.'))

    if menu ==4:
        break
    elif menu==1:
        data=int(input("추가할 데이터를 입력하세요"))
        listdata.append(data)
        print(listdata)
    elif menu==2:
        data=int(input('몇번째 데이터를 수정할까요?'))
        data2=int(input('무엇으로 수정할까요?'))
        listdata[data-1]=data2
        print(listdata)
    elif menu==3:
        data=int(input('몇번째 데이터를 삭제할까요?'))
        listdata.remove(data)
        print(listdata)
        
        