from datetime import datetime
from time import sleep


#  Get target date from user
def input_target_date() -> datetime:
    target_input = input("Enter target date (year, month, day, hour, minute, second): \n")
    #  Remove whitespaces and split user input
    splited_target_string = target_input.strip().split(',')
    #  Create datetime object
    target_date = datetime(year=int(splited_target_string[0]),
                           month=int(splited_target_string[1]),
                           day=int(splited_target_string[2]),
                           hour=int(splited_target_string[3]),
                           minute=int(splited_target_string[4]),
                           second=int(splited_target_string[5]))
    return target_date


#  Calculate difference between now and target date
def diff_calculate(target_date: datetime) -> datetime:
    return target_date - datetime.now()


#  Print countdown
def countdown(target_date: datetime):
    while datetime.now() != target_date:
        delta = diff_calculate(target_date)
        #  Continious print countdown withput milliseconds
        print(f"\nCountdown: {str(delta).split('.', 2)[0]}", end='\r')
        sleep(1)


if __name__ == '__main__':
    target_date = input_target_date()
    countdown(target_date)
