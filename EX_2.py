
def change(money):
    count = 0
    while True:
        if money >= 50:
            money -= 50
            count += 1
            print("50")
            pass
        elif money >= 20:
            money -= 20
            count += 1
            print("20")
            pass
        elif money >= 10:
            money -= 10
            count += 1
            print("10")
            pass
        elif money >= 1:
            money -= 1
            count += 1
            print("1")
            pass
        else:
            break
    return f'რაოდენობა {count }'


change(100)
