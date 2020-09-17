import pygal as pygal
from die import Die

# Create a D6.
die_1 = Die()
die_2 = Die()

# Make some rolls, and store results in a list.
results = [0] * 36
print(len(results))
for roll_num in range(100000):
    roll = die_1.roll() * die_2.roll()
    results[roll - 1] += 1

# Visualize the results.
hist = pygal.Bar()

hist.title = "Result of rolling two D6 1000 times and multiplying their results."
hist.x_labels = list(range(1, 37))
hist.x_title = "Result"
hist.y_title = "Frequence of Result"

hist.add("D6 + D6", results)
hist.render_to_file('dice_visual.svg')
