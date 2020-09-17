import matplotlib.pyplot as plt

input_values = list(range(1, 5000))
squares = [x**3 for x in input_values]

plt.scatter(input_values, squares, c=squares, linewidth=5, cmap=plt.cm.spring, s=40)

# Set chart title and label axes.
plt.title("Square numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
plt.tick_params(axis='both', labelsize=14)

plt.show()
