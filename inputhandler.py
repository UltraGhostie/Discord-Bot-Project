from __future__ import print_function
from createEvent import createEvent


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

    return createEvent(summary, location, description, startTime, endTime, attendees, reminders)
