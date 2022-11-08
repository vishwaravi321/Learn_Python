print("Lists are mutable objects which means it can be manipulatd after creation")


nums = []

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

