def is_leap(year):
    leap = True
    non_leap = False

    if (year%4 == 0):
        if (year%100 == 0):
            if (year%400 == 0):
                return leap
            else:
                return non_leap
        else:
            return leap

    else:
        return non_leap

year = int(input())
print(is_leap(year))
