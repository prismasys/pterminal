import prisma.utils.push as push

print('Send a message to the users:\n')

x = input()

push.msgtopusher(x)

print('Message Sended!')