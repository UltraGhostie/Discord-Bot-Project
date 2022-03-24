def event(input, summary = 'Event', location = 'location', description = 'description', startTime = 1, endTime = -1, attendees = 'null', reminders = '30'): 
    REPLACE = 'test /t test2'
    message = input.split()
    message.pop(0)
    indexlist = []
    for item in message:
        if item.startswith('/'):
            indexlist.append(message.index(item))
            print(item + ':' + str(message.index(item)))
    print(indexlist)
    for index in indexlist:
        if len(message) < index + 1:
            return REPLACE
        match message[index]:
            case '/t':
                print('t')
            case '/a':
                print('a')
        
        if len(indexlist) - 1 < index + 1:
            return REPLACE
    return

if __name__ == '__main__':
    event('test /t test2 /a aszdg')