import copy
import random

class Hat:
    def __init__(self, **kwargs):
        # Initialize the Hat object with balls. **kwargs allows for a dynamic number of ball colors and quantities.
        self.contents = []
        for key, val in kwargs.items():
            # For each color and its quantity, add that many color strings to the contents list.
            self.contents.extend([key] * val)

    def draw(self, balls_to_draw):
        # Draw a specified number of balls from the hat randomly.
        popped_balls = []

        # If the requested number of balls exceeds the total available, return all balls.
        if balls_to_draw > len(self.contents):
            return self.contents

        # Randomly select and remove balls from the hat.
        for _ in range(balls_to_draw):
            ball = random.choice(self.contents)
            self.contents.remove(ball)
            popped_balls.append(str(ball))

        return popped_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    # Conduct an experiment to estimate the probability of drawing a specific combination of balls.

    # Initialize counters for the current experiment and the number of successes.
    curr_exp_count = 0
    success = 0

    # Repeat the experiment num_experiments times.
    while curr_exp_count < num_experiments:
        # Make a deep copy of the hat for each experiment to not alter the original hat.
        hat_copy = copy.deepcopy(hat)
        # Draw balls as specified for the experiment.
        popped = hat_copy.draw(num_balls_drawn)

        # Check if the drawn balls meet the expected criteria.
        flag = False
        for ball, count in expected_balls.items():
            if popped.count(ball) >= count:
                flag = True
                continue
            else:
                flag = False
                break

        # Count the experiment as a success if it meets the expected criteria.
        if flag:
            success += 1

        curr_exp_count += 1

    # Calculate and return the probability of success based on the experiment outcomes.
    return success / num_experiments

# Example usage of the Hat class and experiment function.
hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                         expected_balls={"red": 2, "green": 1},
                         num_balls_drawn=5,
                         num_experiments=2000)

# The probability variable now holds the estimated probability of drawing
# at least two red and one green ball from the specified hat configuration
# over 2000 experiments.
