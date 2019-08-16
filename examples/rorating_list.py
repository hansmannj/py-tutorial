import random

numbers = []
max_numbers = 10

for i in range(20):
    index = len(numbers) % max_numbers
    if len(numbers) < max_numbers:
        numbers.append(random.randint(10, 99))
    else:
        numbers[index] = random.randint(10, 99)
    print(sum(numbers))
