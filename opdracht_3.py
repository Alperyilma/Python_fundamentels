#Opdract_3_a

group_of_people = ["Alex","Eliot","Veronica","Lucy","Wouter","Bart"]

first_chars = [s[0] for s in group_of_people]
print(first_chars)

numbers = list(range(100))
sum = 0
for i in numbers:
    sum += i
print(f"sum: {sum}")

print("-----------------------")

# Opdracht_3_b

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]
fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

# Example for loop solution to add 1 to each number in the list
numbers_plus_one = []

for number in numbers:
    numbers_plus_one.append(number + 1)


# Example of using a list comprehension to create a list of the numbers plus one.
numbers_plus_one = [number + 1 for number in numbers]
print(numbers_plus_one)

# Example for loop solution to do uppercase letter to each fruit in the list
output = []
for fruit in fruits:
    output.append(fruit.upper())

# Example of using a list comprehension to create a list of the numbers
output = [fruit.upper() for i in fruits]
print(output)

print("----------------------------")

#Opdracht_3_c

count = 0
while count < 5:
    number_list = [list(range(10))] * 2
    print(number_list)
    count += 1










