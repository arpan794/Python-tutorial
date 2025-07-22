
# for loop 

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)


for i in range(5):
    print(i)

# while loop

count = 0

while count < 5:
    print("count is:",count)
    count +=1


# break keyword

for i in range(5):
    if i == 2:
        break
    print(i)


# continue keyword

for i in range(5):
    if i == 3:
        continue
    print(i)


# print all even no. from 1 to 10

for i in range(1, 11):
    if i%2 == 0:
        print(i)


#******there is no do while loop in python**********