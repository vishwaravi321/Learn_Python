
obj = []



def List():
    print("So List it is!!!!!!!!!!")
    print(obj)

    print("adding elements to the list")
    obj.append(21)
    print(obj)

    obj.append(2.11)
    print(obj)

    obj.append("Hey")
    print(obj)

    print("Printing specific elements from the string")

    print("First element of the list:")
    print(obj[0])

    print("Second element of the list:")
    print(obj[1])

    print("And so on....!!!")



    print("deleting elements from the string")
    print(obj)
    obj.pop()
    print(obj)

    obj.pop()
    print(obj)

    obj.pop()
    print(obj)
    print(type(obj))

def Dictionary():

    print("So Dictionary it is!!!!!!!!!")

    obj = {'name': 'Vishwa', 'age': '21'}
    print(obj)
    print(type(obj))



choice = input("What is your Choice of object(List/Dictionary):")

if (choice == "Dictionary"):
    Dictionary()
elif (choice == "List"):
    List()
else:
    print("Hey Dude please select from those two,Don't be a douche bag...")




print("After Conditions:")

print(type(obj))
