def event(input, summary='Event', location='location', description='description', startTime=1, endTime=-1, attendees='null', reminders='30'):
    message = input.split('/')
    for item in message:
        message[message.index(item)] = item.strip()
    message.pop(0)
    for flag in message:
        argslist = flag.split(' ')
        match argslist.pop(0):
            case 'n':
                summary = ' '.join(argslist)
            case 'a':
                location = ' '.join(argslist)
            case 'd':
                description = ' '.join(argslist)
            case 's':
                startTime = ' '.join(argslist)
            case 'e':
                endTime = ' '.join(argslist)
            case 'i':
                attendees = ' '.join(argslist)
            case 'r':
                reminders = ' '.join(argslist)
    return


if __name__ == '__main__':
    event('test /n test2 test 3 /a test4 test5')
