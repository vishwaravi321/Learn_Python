import datetime



def compareDates(curDate, postDate, postTime):

    noon = datetime.time(18,0,0)

    if (curDate ==  postDate) and (postTime <= noon):
        print('Allow')
    else:
        print("Don't allow")

def dateConvertion(strDate):
    date = datetime.datetime.strptime(strDate, '%m-%d-%Y').date() 
    print(date)
    return date


date = datetime.datetime.now().date()
time = datetime.datetime.now().time()


conDate = dateConvertion('12-8-2022')

compareDates(date,conDate,time,)







