from yeelight import Bulb, discover_bulbs, TemperatureTransition, SleepTransition, Flow
import time


class BulbControl(object):
    def prepare(self):
        self.bulbIp = discover_bulbs()[0]['ip']
        self.bulb = Bulb(self.bulbIp)
        self.turn_on()
        self.bulb.set_brightness(70)

    def __init__(self):
        self.bulbIp = ''
        self.bulb = None
        self.prepare()

    def turn_on(self):
        self.bulb.turn_on()

    def turn_off(self):
        self.bulb.turn_off()

    def emote(self, emotion):
        # TODO: transfer all rgb colors to an standalone json file
        if (emotion == "Neutral"):
            self.bulb.set_rgb(255, 255, 255)
        if (emotion == "Positive"):
            self.bulb.set_rgb(0, 255, 0)
        if (emotion == "Negative"):
            self.bulb.set_rgb(255, 0, 0)
        if (emotion == "angry"):
            self.bulb.set_rgb(255, 128, 0)  # yellow
        if (emotion == "evil"):
            self.bulb.set_rgb(204, 0, 0)  # red
        if (emotion == "happy"):
            self.bulb.set_brightness(100)
            transitions = [
                TemperatureTransition(1700, duration=400),
                SleepTransition(duration=100),
                TemperatureTransition(6500, duration=400)
            ]

            flow = Flow(
                count=0,
                action=Flow.actions.recover,
                transitions=transitions
            )

            self.bulb.start_flow(flow)


# bulbControl = BulbControl()


# def main():
#     inputEmote = input("\nWhat's your emote? \nangry\nevil\nhappy\n")
#     if (inputEmote == "angry" or inputEmote == "evil" or inputEmote == "happy"):
#         print("\nFine! Setting the mood.\n")
#         bulbControl.emote(inputEmote)
#     else:
#         print("\nSrry, wrong emote!")

#     # bulbControl.turn_off()


# while True:
#     main()
