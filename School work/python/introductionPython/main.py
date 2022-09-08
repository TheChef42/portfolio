print("Hello to Python")

x = 34
print(x)
x = "Daniel"
print(x)

# python is s indented languade

def sum(a, b):
    c = a + b
    return c

def multiply(d, e):
    """
    This function takes two integers and multiply them
    :param d: integer input
    :param e: integer input
    :return: the result
    """
    f = d * e
    return f

def sum_list(list):
    sum = 0
    for x in list:
        sum += x
    return sum


print(sum(3, 6), multiply(3, 6))

#Arrays
mylist = [12, -4, -7, 3, 4, 6]
print(mylist)
print(sum_list(mylist))

mylist.sort()
print(mylist)

print("Working with the second list")

mylist2 = [2, 4, "sokol", 4.12, 5, "aau", 12]
print(mylist2)
print(mylist2[:3]) #slicing
print(mylist2[3:]) #slicing
print(mylist2[2:5]) #slicing
print(mylist2[0]) #2
print(mylist2[-1]) #12
print(mylist2[-2]) #12
#print(mylist2[-8]) #error
print(len(mylist2)) #7



