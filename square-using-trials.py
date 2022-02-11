# given a 1 by 1 square,
# we randomly select two points within the square,
# eg (.25, .4) and (.5, .7).
# From that, we get a distance between the two.
# the question that remains is:
# what is the average length of the distance

import random
import math

# square
width = 1

# the two points
y2 = 0.0
y1 = 0.0
x2 = 0.0
x1 = 0.0

distance = 0.0

trials = 10000000

for i in range(trials):
    y2 = random.uniform(0, 1)
    y1 = random.uniform(0, 1)
    x2 = random.uniform(0, 1)
    x1 = random.uniform(0, 1)

    distance += math.sqrt((y2-y1)**2 + (x2-x1)**2)

print(distance/trials)
