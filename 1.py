# """import math
# rayon = int(input("Enter the radius of the circle: "))
# surface = int(math.pi * pow(rayon,2))
# print(f"the surface of the circle is: {surface}") """"

def main():
    def enter():
        num1 = int(input("enter the first number: "))
        num2 = int(input("enter your second number: "))
        num3 = int(input("enter your therd number: "))
        numbers = (num1 + num2 + num3) / 3

numbers = []
n = int(input("Enter the size of inputs: "))
for i in range(n):
    j = i + 1
    note = float(input(f"Enter note number {j}: "))
    numbers.append(note)
summ = 0
for y in range(n):
    summ = summ + numbers[y]
average = summ / n
main()
print("The average is: ",average) 