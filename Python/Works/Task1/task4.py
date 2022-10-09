import time
import datetime


def timer(tm: str):
    t = time.strptime(tm, '%H:%M:%S')
    total_seconds = datetime.timedelta(hours=t.tm_hour, minutes=t.tm_min, seconds=t.tm_sec).total_seconds()
    while total_seconds > 0:
        current_time = str(datetime.timedelta(seconds=total_seconds))
        print(current_time)
        time.sleep(1)
        total_seconds -= 1

    print("Время вышло!")


if __name__ == '__main__':
    timer('12:55:01')
