import datetime

def compareDates(curDate, postDate, postTime):
    noon = datetime.time(12,0,0)
    if (curDate ==  postDate) and (postTime <= noon):
        print('Allow')
    else:
        print("Don't allow")


def dateConvertion(strDate):
    date = datetime.datetime.strptime(strDate, '%d-%m-%Y').date() 
    return date

date = datetime.datetime.now().date()

time = datetime.datetime.now().time()

conDate = dateConvertion(input("Enter Date in 'dd-mm-2022':"))

compareDates(date,conDate,time,)







