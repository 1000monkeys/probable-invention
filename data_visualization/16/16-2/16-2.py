import csv
from datetime import datetime

from matplotlib import pyplot as plt

# Get high temperatures from file.
with open('death_valley_2014.csv') as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dv_dates, dv_highs, dv_lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dv_dates.append(current_date)
            dv_highs.append(high)
            dv_lows.append(low)

with open('sitka_weather_2014.csv') as f:
    reader = csv.reader(f)
    header_row = next(reader)

    sitka_dates, sitka_highs, sitka_lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            sitka_dates.append(current_date)
            sitka_highs.append(high)
            sitka_lows.append(low)

# Plot data.
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(sitka_dates, sitka_highs, c='orange')
plt.plot(sitka_dates, sitka_lows, c='green')
plt.fill_between(sitka_dates, sitka_highs, sitka_lows, facecolor='blue', alpha=0.1)

plt.plot(dv_dates, dv_highs, c='red')
plt.plot(dv_dates, dv_lows, c='blue')
plt.fill_between(dv_dates, dv_highs, dv_lows, facecolor='green', alpha=0.1)

# Format plot.
plt.title("Daily high and low temperatures - 2014\nDeath Valley, CA & Sitka", fontsize=24)
plt.xlabel('', fontsize=20)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
