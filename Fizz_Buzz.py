import time

while True:

    num = int(input("give a numnber to count up to, enter 000 to end the game"))
    count_num = 1
    if num == 000:
        break

    while num >= count_num:

        if count_num % 15 == 0:
            print("fizzbuzz")
            time.sleep(1)

        elif count_num % 3 == 0:
            print("fizz")

        elif count_num % 5 == 0:
            print("buzz")

        else:
            print(count_num)
        count_num += 1


