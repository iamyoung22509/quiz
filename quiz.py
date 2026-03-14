import random
score = 0
while True:
    a = random.randint(1,20)
    b = random.randint(1,20)

    print("\n문제:", a, "+", b, "=?")

    answer = a + b

    user = input("답 입력 (종료 q):")

    if user == "q":
        break
    
    if int(user) == answer:
        print("정답!")
        score += 1
    else:
        print("틀림. 정답:", answer)
    
    print("현재 점수:", score)