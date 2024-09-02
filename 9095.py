c = int(input())
for _ in range(c):
    number = int(input())

    num_list = [1,2,4]

    if number == 1:
        print(num_list[0])
    elif number == 2:
        print(num_list[1])
    elif number == 3:
        print(num_list[2])
    else:
        count = 3
        while count != number:
            num_list.append(num_list[count - 1] + num_list[count - 2] + num_list[count - 3])
            count += 1
        print(num_list[number - 1])
