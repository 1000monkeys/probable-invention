import pygal as pygal
from die import Die

# Create a D6.
die_1 = Die()
die_2 = Die()
die_3 = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
for value in range(3, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
hist = pygal.Bar()

hist.title = "Result of rolling three D6 1200 times."
hist.x_labels = list(range(3, 19))
hist.x_title = "Result"
hist.y_title = "Frequence of Result"

hist.add("D6 + D6 + D6", frequencies)
hist.render_to_file('dice_visual.svg')
