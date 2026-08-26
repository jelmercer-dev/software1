first = 1

while first <= 5:
    second = 1
    while second <= 5:
        print(f"{first} times {second} is {first*second:d}")
        second = second + 1
    first = first + 1
