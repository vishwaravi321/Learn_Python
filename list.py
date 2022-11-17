print("Lists are mutable objects which means it can be manipulatd after creation")


nums = [21,3.45]
    
print(type(nums))
print(nums)

print("adding elements to the list")
nums.append(21)
print(nums)

nums.append(2.11)
print(nums)

nums.append("Hey")
print(nums)

print("Printing specific elements from the string")

print("First element of the list:")
print(nums[0])  

print("Second element of the list:")
print(nums[1])

print("And so on....!!!")



print("deleting elements from the string")
print(nums)
nums.pop()
print(nums)

nums.pop()
print(nums)

nums.pop()
print(nums)

my = ['a']
print("list my",my)

my.extend(nums)
print("list my",my)

my.insert(0,45)
my.insert(5,45) # similiar to .append but we can choose the index we want to add
print("list my",my)
