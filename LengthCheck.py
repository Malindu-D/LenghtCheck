list = []

for i in range(10):
    print("Enter",i+1,end=" ")
    uint =input("Name: ")
    list.append(uint)


def check_length(list):
    count = 0
    for j in list:
        if len(j) > 5:
            count += 1

    return count

x = check_length(list)

print(x," Names have more than 5 letters: ")
