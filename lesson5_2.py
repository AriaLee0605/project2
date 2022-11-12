import random
random.random()

print(random.uniform(1,10))
print(random.uniform(99,100))



min = 1
max = 10
count = 0
random_value = random.randint(min,max)
print("＝＝＝＝＝＝＝猜數字遊戲＝＝＝＝＝＝＝")
while True:
    count += 1
    keyin = int(input(f"猜數字範圍{min}~{max}:"))
    if keyin >= min and keyin <= max :
        if(keyin == random_value):
            print(f"猜對了,答案是:{random_value}")
            print(f"您總共猜{count}次")
            break
        elif keyin > random_value:
            print("再小一點")
            max = keyin - 1
        elif keyin < random_value:
            print("再大一點")
            min = keyin + 1
        print(f"您已經猜了{count}次")
    else:
        print("超出範圍")

print("遊戲結束")