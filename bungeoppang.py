cart = []

while True:
    print("\n=== 붕어빵 가게===")
    print("1. 붕어빵 담기")
    print("2. 장바구니 보기")
    print("3. 장바구니에서 빼기")
    print("4. 주문 종료")

    choice = input("원하는 메뉴를 선택하세요.")

    if choice == "1":
        fish = input("어떤 붕어빵을 담으실래요? (팥붕 / 슈붕): ")
        
        if fish == "팥붕" or fish == "슈붕":
            cart.append(fish)
            print(f"{fish}이 장바구니에 담겼습니다!")
        else:
            print("❌ 없는 주문입니다. '팥붕' 또는 '슈붕'만 입력해주세요.")

    elif choice == "2":
        print("=== 현재 장바구니 목록 ===")
        print(cart)

    elif choice == "3":
        print(f"=== 현재 장바구니 목록 ===: {cart}")
        remove_fish = input("장바구니에서 뺄 붕어빵 이름을 정확히 입력하세요: ")

        if remove_fish in cart:
            cart.remove(remove_fish)
            print(f"🗑️ {remove_fish}을 장바구니에서 뺐습니다.")
        else:
            print("❌ 장바구니에 해당 붕어빵이 없습니다.")

    elif choice == "4":
        print("주문을 종료합니다.")
        break
