from datetime import datetime, timedelta

# Starting date and time
start_time = datetime(2024, 8, 25, 12, 0, 0)

# List to store the times
times = []

# Loop to increment hours and store the times
for i in range(10):
    times.append(start_time.strftime("%Y-%m-%d %H:%M:%S"))
    start_time += timedelta(hours=3)

# Print the times
for time in times:
    print(time)
