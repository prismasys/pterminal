from notify_run import Notify

notify = Notify()

print(notify.register())

stop = 0

while stop == 0:
    print('\n')
    print('1 - To stop this environment\n')
    print('2 - To send test message\n')
    print('3 - To send a custom message\n')
    print('\n---------------------------\n')
    inpoot = int(input())

    if inpoot == 1:
        stop = 1
    elif inpoot == 2:
        notify.send('Haha poo poo')
        continue
    elif inpoot == 3:
        print('Enter message')
        msg = input()
        notify.send(msg)
        continue
    else:
        continue



