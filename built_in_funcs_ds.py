# Built in Functions for Data Structures...

'''____zip___'''

day = ['Monday', 'Tuesday', 'Wednnesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

muscle_group = ['Chest', 'Back', 'Shoulder', 'Biceps', 'Triceps', 'Leg', 'Rest']

data = zip(day,muscle_group)
print(data) #unreadable format but can be changed to desired DS.......

print("Printing as List")
print(list(data)) # Printing as list...
print("Printing as Dictionary")
print(dict(data)) # Printing as dictionary...
print("Printing as tuple")
print(tuple(data)) # Printing as tuple...

print("Printing as list:")
print(list(zip(day,muscle_group)))
print("Printing as Dict:")
print(dict(zip(day,muscle_group)))
print("Printing as tuple:")
print(tuple(zip(day,muscle_group)))