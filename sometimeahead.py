import datetime
def main(delta = 1):
    time = datetime.datetime.today().isoformat('T','seconds')
    hour = time[time.index('T') + 1]
    timedate = time.split('T')
    timedate[1].replace(hour, str(int(hour) + delta))
    time = 'T'.join(timedate)
    return time