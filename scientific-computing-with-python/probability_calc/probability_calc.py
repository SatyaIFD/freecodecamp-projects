import copy  # To make deep copies of our hat object so experiments don’t affect each other
import random  # To randomly pick balls from the hat
from collections import Counter  # To count how many of each color we drew easily

class Hat:
    def __init__(self, **kwargs):
        """
        When you create a Hat, you tell it how many balls of each color it contains.
        For example: Hat(red=5, blue=3) means 5 red balls and 3 blue balls.
        """
        self.contents = []  # This list will hold the color of every single ball in the hat
        
        # Now, for each color and its count, add that many strings to contents
        for color, count in kwargs.items():
            for _ in range(count):
                self.contents.append(color)
        # At this point, self.contents is something like ['red', 'red', 'red', 'red', 'red', 'blue', 'blue', 'blue']

    def draw(self, num_balls_to_draw):
        """
        This method simulates drawing balls from the hat without putting them back.
        You tell it how many balls to draw.
        If you ask for more balls than the hat has, it gives you all the balls left.
        """
        drawn_balls = []  # This will store the balls we draw

        # If requested number is more than or equal to what's available, just take everything
        if num_balls_to_draw >= len(self.contents):
            drawn_balls = self.contents[:]  # Copy all balls
            self.contents = []  # Empty the hat since all balls are drawn
            return drawn_balls

        # Otherwise, draw one ball at a time
        for _ in range(num_balls_to_draw):
            chosen_ball = random.choice(self.contents)  # Pick a random ball
            drawn_balls.append(chosen_ball)  # Add it to our drawn balls
            self.contents.remove(chosen_ball)  # Remove it from the hat (no replacement!)

        return drawn_balls  # Return the list of drawn balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    """
    This function estimates the probability of drawing the expected balls from the hat.

    Steps:
    1. Run many experiments (num_experiments times).
    2. Each time, create a fresh copy of the hat (so we don't mess up the original).
    3. Draw the requested number of balls.
    4. Check if the drawn balls meet the expected criteria (at least as many balls of each color).
    5. Count how many experiments are successful.
    6. Calculate probability = (number of successful experiments) / (total experiments).
    """

    successful_experiments = 0  # Counter for how many times we got the expected balls

    for _ in range(num_experiments):
        temp_hat = copy.deepcopy(hat)  # Make a fresh copy so each experiment is independent
        drawn_balls = temp_hat.draw(num_balls_drawn)  # Draw balls from the copied hat
        drawn_counts = Counter(drawn_balls)  # Count how many of each color we got

        # Assume success until proven otherwise
        is_success = True

        # Check if we have at least the expected count for each color
        for color, count_expected in expected_balls.items():
            if drawn_counts[color] < count_expected:
                is_success = False  # Not enough balls of this color, so fail this experiment
                break  # No need to check further

        if is_success:
            successful_experiments += 1  # We got the expected balls this experiment

    # Finally, calculate probability by dividing successes by total experiments
    probability = successful_experiments / num_experiments
    return probability
