import pygal as pygal
from die import Die

# Create a D6.
die_1 = Die()
die_2 = Die(10)

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1200):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
hist = pygal.Bar()

hist.title = "Result of rolling one D6 and D10 1200 times."
hist.x_labels = list(range(2, 16))
hist.x_title = "Result"
hist.y_title = "Frequence of Result"

hist.add("D6 + D10", frequencies)
hist.render_to_file('dice_visual.svg')
