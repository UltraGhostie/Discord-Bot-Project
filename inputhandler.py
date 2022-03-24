from __future__ import print_function
from createEvent import createEvent


def event(input, summary = 'Event', location = 'location', description = 'description', startTime = 1, endTime = -1, attendees = 'null', reminders = '30'): 
    message = input.split()
    message.pop(0)
    indexlist = []
    for item in message:
        if item.startswith('/'):
            indexlist.append(message.index(item))
            print(item + ':' + str(message.index(item)))
    print(indexlist)
    for index in indexlist:
        if len(indexlist) > indexlist.index(index) + 1:
            if index + 1 == indexlist[indexlist.index(index) + 1]:
                return 'empty'
        if len(message) < index + 1:
            return createEvent()
        match message[index]:
            case '/n':
                summary = message[index + 1]
            case '/a':
                location = message[index + 1]
            case '/d':
                description = message[index + 1]
            case '/s':
                startTime = message[index + 1]
            case '/e':
                endTime = message[index + 1]
            case '/i':
                attendees = message[index + 1]
            case '/r':
                reminders = message[index + 1]
        
        if len(indexlist) - 1 < index + 1:
            return createEvent(summary, location, description, startTime, endTime, attendees, reminders)
    return createEvent()