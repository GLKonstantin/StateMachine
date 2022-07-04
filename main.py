from statemachine import StateMachine, State
from time import sleep


class TrafficLightMachine(StateMachine):
    green = State('* Зеленый', initial=True)
    yellow = State('**** Желтый')
    red = State('******** Красный')
    white = State('***************** Белый')

    slowdown = green.to(yellow)
    stop = yellow.to(red)
    go = red.to(white)
    raketa = white.to(green)

    cycle = green.to(yellow) | yellow.to(red) | red.to(white) | white.to(green)


traffic_light = TrafficLightMachine()

while True:
    traffic_light.cycle()
    print(traffic_light.current_state.name)
    sleep(1)

# traffic_light.cycle()
#
# traffic_light.cycle()
#
# traffic_light.cycle()

