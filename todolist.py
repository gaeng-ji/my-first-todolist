todo_list = []

while True:

    print("\n=== 투두리스트 메뉴===")
    print("1. 할 일 추가")
    print("2. 할 일 목록 보기")
    print("3. 프로그램 종료")

    menu = input("원하는 메뉴 번호를 입력하세요.")

    if menu == "1":
        todo = input("추가할 할 일을 입력하세요: ")
        todo_list.append(todo)
        print("추가되었습니다!")

    elif menu == "2":
        print("=== 현재 내 할 일 목록 ===")
        print(todo_list)

    elif menu == "3":
        print("프로그램을 종료합니다.")
        break