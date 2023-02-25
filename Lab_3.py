#
#Вакантное место
#

#просто варики списков(2)
list_of_nums_1 = []
for i in range(5):
    list_of_nums_1.append(i)

list_of_nums_2 = list(range(5))

print(list_of_nums_1)
print(list_of_nums_2)

#вариант реализации range для флоата
def float_range(start, stop=None, step=1):
    start = float(start)
    if stop == None:
        stop = start
        start = 0.0
    if step == 0.0:
        print("[empty(step==0)]")
        return []
    
    print("[", end="")
    step_counter = 0
    while True:
        tmp = float(start + step_counter * step)
        if step > 0 and tmp >= stop:
            break
        if step < 0 and tmp <= stop:
            break

        step_counter += 1
        yield tmp
    print("]")


# Тесты созданного метода float
#list_of_nums_3 = []
for i in float_range(0, 10, 0.5):
    print(i,end=", ")

for i in float_range(0, 10, 0):
    print(i,end=", ")

for i in float_range(0, 4.6):
    print(i,end=", ")

for i in float_range(10):
    print(i,end=", ")


#3й пункт - задачи:
#1я 
A = int(input("Enter the first number: "))
B = int(input("Enter the second number: "))

for i in range(A, B + 1):
    print(i)

#2я 
A = int(input("Enter the first number: "))
B = int(input("Enter the second number: "))

if A < B:
    for i in range(A, B + 1):
        print(i)
else:
    for i in range(A, B - 1, -1):
        print(i)

#3я 
A = int(input("Enter the first number: "))
B = int(input("Enter the second number: "))

for i in range(A, B - 1, -2):
    print(i)

# 4я 
print("Rules of the Gamr:")
print("Cards are unique - do NOT enter value of a card again!")

print("Enter Number of cards or letter N to exit: ")

N = int(input())

expected_sum = N * (N + 1) // 2
actual_sum = 0
for i in range(1, N):
    print("Enter %g value: " % i)
    card = int(input())
    actual_sum += card

lost_card = expected_sum - actual_sum
print("Ur card is", lost_card)


