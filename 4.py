random_nums = input("Enter random numbers for your list (e.g: 8 5 3 9 1 7): ")
random_list = [int(x) for x in random_nums.split()]
for i in range(len(random_list)):
    for j in range(0, len(random_list) - i -1):
        if random_list[j] > random_list[j+1]:
            random_list[j], random_list[j+1] = random_list[j+1], random_list[j]
print("Your ordered random numbers is: ", random_list)
