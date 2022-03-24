import datetime


def main(delta=1):
    time = datetime.datetime.today().isoformat('T', 'seconds')
    hour = time[time.index('T') + 1] + time[time.index('T') + 2]
    timedate = time.split('T')
    timedate[1] = timedate[1].replace(hour, str(int(hour) + int(delta)), 1)
    time = 'T'.join(timedate)
    return time


if __name__ == '__main__':
    main()
