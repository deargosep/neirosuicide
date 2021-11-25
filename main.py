import sys
from lib.sound import Sound
from data.json import read, check

# initializing things
sound = Sound()
args_length = len(sys.argv)
# print(f"args length: {args_length}")


class Talk(object):
    def __init__(self):
        if args_length >= 3:
            self.depression = sys.argv[2]
        else:
            self.depression = 0
        if args_length >= 2:
            self.input = sys.argv[1]
        else:
            self.input = 'text'
        sound.setInput(self.input)
        print("input type:", self.input)
        print("depression level:", self.depression)

    def setInput(self, value: str):
        self.input = value
        sound.setInput = value

    def increment(self, value=1):
        self.depression += value
        print("\nуровень депрессии:", self.depression)
        sound.say('ай блять')

    def decrement(self, value=1):
        self.depression -= value
        print("\nуровень депрессии:", self.depression)
        sound.say('спасибо')

    def reset():
        self.depression = 0
        print('reseted')


siri = Talk()


def main():
    sound.say('привет, напиши или скажи мне что нибудь ')
    userType = sound.listenTo()
    sound.say("читаю:" + userType)
    sound.say('хм..')
    if check(userType) == 'bad':
        siri.increment()
    elif check(userType) == 'good':
        siri.decrement()
    else:
        sound.say('чего?')

    # if :
    # elif userType in read():
    #     Talk().decrement()
    # else:


while True:
    main()
