Workouts = ['chest', 'Back', 'Shoulder', 'Biceps', 'triceps', 'Legs', 'Rest']
Days = ['Monay', 'Tuesday', 'Wednesday', 'Thursday', 'Friday' , 'Saturday', 'Sunday']

schedule = {}

for i in range(len(Days)):
    schedule[Days[i]] = Workouts[i]



print(Workouts)
print(Days)
print(schedule)
sche = zip(Days,Workouts)

print(dict(sche))
print(list(sche))