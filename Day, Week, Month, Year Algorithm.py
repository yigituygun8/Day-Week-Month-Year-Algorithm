# Create a for loop that will increase from 1 to N (take user input) consistenly and increase year variable every 365 days
# also, increase month variable every 30 days, week variable every 7 days and day variable every 1 day


day = 0
week = 0 
month = 0
year = 0

# 1 year = 365 days || 1 month = 30 days || 1 week = 7 days 

howmany = int(input("How Many Days Do You Want?: "))

for i in range(howmany):
    day += 1

for j in range(day // 7):
    week += 1

for k in range(day // 30):
    month += 1

for n in range(day // 365):
    year += 1

print("Day:",day,"\n"+"Week:",week,"\n"+"Month:",month,"\n"+"Year:",year)




            




