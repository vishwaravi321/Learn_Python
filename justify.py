obj = []

choice = input("What is your Choice of object(List/Dictionary):")

if (choice == "Dictionary"):
    obj = {'name': 'Vishwa', 'age': '21'}
    print(obj)
    print(type(obj))
elif (choice == "List"):
    obj = ['name', 'Vishwa', 'age', '21']
    print(obj)
    print(type(obj))
else:
    print("Hey Dude please select from those two,Don't be a douche bag...")


print("After conditions:")
print(type(obj))