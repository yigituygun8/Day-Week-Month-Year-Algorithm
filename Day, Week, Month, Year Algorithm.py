# Create a for loop that will increase from 1 to N (take user input) consistenly and increase year variable every 365 days
# also, increase month variable every 30 days, week variable every 7 days and day variable every 1 day



import time

print("Counting the days... (Press Ctrl+C to terminate)")

try:
    day = 0
    week = 0
    month = 0
    year = 0
    while(True):
        for i in range(365):
            day += 1
            time.sleep(0.3)
            if day % 7 == 0:
                week += 1
                time.sleep(0.3)
            if day % 30 == 0:
                month += 1
                time.sleep(0.3)
            if day % 365 == 0:
                year += 1
                time.sleep(0.3)
        if i == 364:
            print("Day:", day, "\n"+"Week:", week, "\n" + "Month:", month, "\n"+"Year:", year)
            break


except KeyboardInterrupt:
    print("Day:", day, "\n"+"Week:", week, "\n" + "Month:", month, "\n"+"Year:", year)
    pass




            




