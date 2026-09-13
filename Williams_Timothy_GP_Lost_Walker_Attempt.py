import random
import math


class Walker:
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def __init__(self, initial_position=(0, 0)): #Sets the initial position of walker to origin
        self.initial_position = initial_position
        self.position = initial_position
        self.returns = [initial_position]

    def random_walk(self, steps):
        for _ in range(steps):
            direction = random.choice(self.directions)   #Chooses randomly from 4 fixed directions on coordinate plane
            self.position = (
                self.position[0] + direction[0],
                self.position[1] + direction[1],
            )
            self.returns.append(self.position)
        return self.position


class Lostwalker(Walker):  # Passes class walker to LostWalker for inheritance
    pass


steps = int(input("How many steps is the walker taking? "))


def random_steps_distance():
    walker = Lostwalker()
    final_position = walker.random_walk(steps)
    distance = math.hypot(
        final_position[0] - walker.initial_position[0],
        final_position[1] - walker.initial_position[1],
    )
    print(
        "The walker has taken", steps,
        "steps and is now at position:", final_position,
        "with a distance of", round(distance, 2), "from the origin."
    )
    return distance


random_steps_distance()

n = 0
dist__ = []
i = int(input("How many simulations would you like to run? "))
while n < i:
    random_steps_distance()
    dist__.append(round(random_steps_distance(), 2))
    n += 1

if n == i:
    print("You have completed", i, "simulations.")
    average_distance = sum(dist__)/len(dist__)
    print("The average distance from the origin after", i, "simulations is:", round(average_distance, 4))

else:
    print("You have completed ", n, " simulations.")