import numpy as np
import matplotlib.pyplot as plt
import random
from IPython import display

DOOR_AMOUNT = 3


def main():
    run = True
    switch = no_switch = 0
    tests = 0
    plt.ion()
    while run:
        display.clear_output(wait=True)
        display.display(plt.gcf())
        plt.clf()
        door = np.zeros(DOOR_AMOUNT, dtype=int)  # 3 doors
        door[random.randint(0, DOOR_AMOUNT - 1)] = 1
        choice = random.randint(0, DOOR_AMOUNT - 1)
        # if you stick to your choice
        if door[choice] == 1:
            no_switch += 1
        # monty
        numbers = np.arange(DOOR_AMOUNT, dtype=int)
        monty = numbers.tolist()
        monty.remove(choice)
        while len(monty) > 1:
            monty_rand = random.randint(0, len(monty) - 1)
            if door[monty[monty_rand]] == 0:
                monty.remove(monty[monty_rand])
        if door[monty] == 1:
            switch += 1

        tests += 1

        data = {'no switch': no_switch / tests * 100, 'switch': switch / tests * 100}
        courses = list(data.keys())
        values = list(data.values())

        plt.bar(courses, values, color='#398db8',
                width=0.5)
        plt.ylim(ymax=100)
        plt.ylabel("% percent chance")
        plt.title("Monty Hall Problem")
        plt.show(block=False)
        plt.pause(.01)
        if not plt.fignum_exists(1):
            run = False


if __name__ == '__main__':
    main()
