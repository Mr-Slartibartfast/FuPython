import random

probability = random.random()
print(probability)

import random

trials = 10000
heads = 0

for _ in range(trials):
    if random.random() < 0.5:  # 50% chance
        heads += 1

estimated_probability = heads / trials
print("Estimated probability of heads:", estimated_probability)