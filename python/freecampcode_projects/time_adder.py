def add_time(start,duration,day='none'):
    week = {'Monday': 1,'Tuesday': 2,'Wednesday': 3,'Thursday': 4,'Friday': 5,'Saturday': 6,'Sunday':7}
    case_insensitive_week={k.casefold(): v for k, v in week.items()}
    start_time,notation=start.split()
    add_hour,add_minute=duration.split(':')
    add_hour=int(add_hour)
    add_minute=int(add_minute)
    hour,minute=start_time.split(':')
    hour=int(hour)
    minute=int(minute)
    add_day=0
    new_day_no=0
    result_message=None
    if notation== 'PM':
        hour+=12     
    result_hour=hour+add_hour
    result_minute=minute+add_minute
    while(result_minute>59):
        result_hour+=1
        result_minute-=60
    add_day=int(result_hour/24)
    while(result_hour>24):
        result_hour-=24
    if result_hour<24 and result_hour>=12:
        notation='PM'
    else:
        notation='AM'
    if result_hour>12: result_hour-=12
    if add_day==1:
        result_message='next day'
    elif add_day>1:
        result_message=str(add_day)+' days later'
    if day.lower() !='none':
        new_day_no=(case_insensitive_week[day.lower()]+add_day-1)%7+1
    if result_message is  None:
        print(f'{result_hour:02d}:{result_minute:02d} {notation}\n' if day == 'none' else f'{result_hour:02d}:{result_minute:02d} {notation},{list(week.keys())[new_day_no-1]}\n')
    else:
        print(f"{result_hour:02d}:{result_minute:02d} {notation},({result_message})\n" if day == 'none' else f"{result_hour:02d}:{result_minute:02d} {notation},{list(week.keys())[new_day_no-1]},({result_message})\n" ) 
def tester(time):
    value,notation=time.split()
    hour,minutes=value.split(':')
    hour=int(hour)
    minutes=int(minutes)
    if hour>12 or minutes>59:
        print('Invalid time')
        exit(0)
def main():
    print("Enter the current Time and Time to add with todays day(optional).\n")
    print("->Example('12:00 AM','5:00','sunday')\n")
    time=input("Enter the current Time:\n")
    tester(time)
    add_value=input("Enter the time to add:\n")
    day=input("Enter the day(optional):\n")
    add_time(time,add_value,day)
if __name__ == '__main__':
    main()
