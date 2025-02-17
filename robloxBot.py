import keyboard, time, random, mouse
from art import tprint

tprint('RobloxBot?')

print("github - https://github.com/starfoxbw/robloxbot/releases")
print("donationalerts - https://donationalerts.com/r/starfoxbw")
print("version 2.2\n")

choice = []
qmsgs = int(input("Write the number of messages/Напишите количество сообщений: "))
inputtime = int(input("Write the interval between messages/Напишите промежуток между сообщениями: "))



for j in range(qmsgs):
    choice.append(str(input("Write a message/Напишите сообщение: ")))


def text(a):
    keyboard.write(random.choice(a))
    keyboard.send("Enter")

def send():
    if keyboard.is_pressed('f9'):
        exit()

    time.sleep(inputtime)
    text(a=random.choice(choice))


for i in range(int(input("Write how many times to send a message/Напишите сколько раз отправить сообщение: "))):
    send()
