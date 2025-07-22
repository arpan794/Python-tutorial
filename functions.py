def greet ():
    print ("hello")

greet()


def greet_user (name):
    print(f"hello, {name}!")

greet_user("alice")



def add(a,b):
    return a+b

result = add(3,5)
print("sum is:",result)



def add_num(a,b):
    return a + b

a = int(input("enter the 1st no. :"))
b = int(input("enter the 2nd no. :"))
result = add_num(a,b)
print("sum is:",result)



def is_even(n):
    if n%2 == 0:
        return True
    else:
        return False
    
result = is_even(8)
print("No. is even:", result)



def is_even(n):
    return n % 2 == 0

# Test the function
print(is_even(4))   # True
print(is_even(7))   # False



         
