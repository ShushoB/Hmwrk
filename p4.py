year = int(input("Enter a year: "))
count = 0
y = 1600
while y <= year:
    if ((y % 4 == 0 and y % 100 != 0) or y % 400 == 0):
        count += 1
    y += 1
print ("The number of lear years from 1600 and " , year, " is: ", count)
